#!/opt/homebrew/bin/bash
## !/bin/bash
# Created by Sergi Ortiz Ropero @ 15/03/2025
# COSAN ROTATIONAL SCAN GAUSSIAN INPUT GENERATION

# parse flags
input_dir=''        # where the files are
num_structures=''   # number of structures
charge=0
multiplicity=1
processors=16

print_usage() {
    printf "\e[1mUsage:\e[0m\n"
    printf '%b\n' "-i\tINPUT FILE\tLigand input structure. See -f for the input format"
    printf '%b\n' "-f\tINPUT FORMAT\tLigand input structure format. Supported: pdb or mol2"
    printf '%b\n' "-o\tOUTPUT NAME\tName of the output files. Default same as input ligand name."
    printf '%b\n' "-c\tCHARGE\t\tGlobal charge of the ligand. Default 0."
    printf '%b\n' "-m\tMULTIPLICITY\tSpin multiplicity of the ligand, computed as 2S+1. Default 1 (singlet)."
    printf '%b\n' "-p\tPROCESSORS\tNumber of processors to use for the Gaussian Job. Default 16."
    printf "\n"
    printf '%b\n' "\e[1mObs.\e[0m \e[0m This script will generate a subdir where the ligand structure is located with the Gaussian job and a log file. Use that dir for everything RESP related.\e[0m"
    printf "\n"
    printf '%b\n' "\e[1mExample.\e[0m bash resp_job_gen.sh -i <ligand>.pdb -f pdb -c 0 -m 1 -p 16"
    printf "\n"
}

while getopts 'i:n:c:m:p:h' flag; do
  case "${flag}" in
    i) input="${OPTARG}" ;;
    n) num_structures="${OPTARG}" ;;
    c) charge="${OPTARG}" ;;
    m) multiplicity="${OPTARG}" ;;
    p) processors="${OPTARG}" ;;
    h)
       print_usage
       exit 0 ;;
    *)
       print_usage
       exit 0 ;;
  esac
done


script_name=$(basename "$0")
printf "Generating a COSAN Gaussian16 job with $script_name\n"
printf '%(%d-%m-%Y %H:%M:%S)T\n' -1

#==========================#
#       PREPROCESSING      #
#==========================#


# obtain ligand base name
LIG_NAME="COSAN"

# create subdirs and move there
SUBDIR="$PWD/"$LIG_NAME"-scan"
echo "creating $SUBDIR"
mkdir $SUBDIR

#========================#
#       SCRIPT CORE      #
#========================#


algo=$(($num_structures - 1))
for ((i = 0 ; i < $num_structures ; i++)); do 
    FILE="$input/cosan_conf_$i.gjf"
    echo $FILE

    # modify charge and multiplicity
    NEW_LINE=" $charge   $multiplicity"
    G_CHG_MULT=$(sed '5q;d' $FILE)
    echo "current chg and mult: $G_CHG_MULT"
    sed -i '' "5s,.*,$NEW_LINE," "$FILE"
    G_CHG_MULT=$(sed '5q;d' $$FILE)
    echo "new chg and mult:    $G_CHG_MULT"

    # modify .com input message
    sed -i '' "3s,.*,$LIG_NAME rotatamer scan $i out of $algo," "$FILE"

    # add number of processors and memory
    sed -i '' '1i\'$'\n''%nprocshared=16'$'\n' "$FILE"
    sed -i '' '2i\'$'\n''%mem=2GB'$'\n' "$FILE"

    # change chk
    sed -i '' '3i\'$'\n'"%chk=/home/sortiz/$LIG_NAME-scan/"$LIG_NAME"_$i.chk"$'\n' "$FILE"

        # add method and basis set
    sed -i '' "4s,.*,# wb97x/6-31g(d)," "$FILE"

    cp $FILE $SUBDIR
done


# create the slurm script to batch the job for Picard
G_JOB_NAME="job_$LIG_NAME.slm"
echo "generating $G_JOB_NAME"
cat > "$SUBDIR/$G_JOB_NAME" <<EOF
#!/bin/bash
#SBATCH -J $LIG_NAME-scan.%j
#SBATCH -e /home/sortiz/$LIG_NAME-scan/$LIG_NAME-scan.%j.err
#SBATCH -o /home/sortiz/$LIG_NAME-scan/$LIG_NAME-scan.%j.out
#SBATCH -p normal
#SBATCH -n 1
#SBATCH -c 16
#SBATCH -t 4-02:00
# script generated automatically by cosan_job_gen.sh
# COSAN scan
# Gaussian job 

# gaussian settings
ml Gaussian/16.C.02-AVX2
#ml Gaussian/16.B.01-LEGACY 

export GAUSS_SCRDIR=\$SLURM_SUBMIT_DIR
printf "gaussian dir:\t\$GAUSS_SCRDIR\n"


# copy the files to temp
for ((i = 0 ; i < $num_structures ; i++)); do 
    FILE="/home/sortiz/$LIG_NAME-scan/cosan_conf_\$i.gjf"
    echo \$FILE
    cp \$FILE \$TMP_DIR  
done 

cd \$TMP_DIR

# actual computation
for ((i = 0 ; i < $num_structures ; i++)); do 

    INPUT_FILES=cosan_conf_\$i.gjf

    printf "\$i start: \`date\`\n"
    srun g16 < \$SLURM_SUBMIT_DIR/\$INPUT_FILES > \$SLURM_SUBMIT_DIR/cosan_conf_\$i.log
    printf "\$i finish: \`date\`\n"

done 
EOF
cat "$SUBDIR/$G_JOB_NAME"
chmod +x "$G_JOB_NAME"





# instruct the user to copy the directory to Picard
printf "\n\n"
printf "Access Picard and create /home/sortiz/\n\n"
printf "Use\n\n\tscp -r $SUBDIR sortiz@158.109.174.75:/home/sortiz/\n\nto copy the files to Picard"
printf "\n\n"
printf "Use\n\n\tscp -r sortiz@158.109.174.75:/home/sortiz/$SUBDIR $PWD \n\nto copy the results from Picard once the job is finished"
printf "\n\n"





exit 0