import cPickle, base64
try:
	from SimpleSession.versions.v65 import beginRestore,\
	    registerAfterModelsCB, reportRestoreError, checkVersion
except ImportError:
	from chimera import UserError
	raise UserError('Cannot open session that was saved in a'
	    ' newer version of Chimera; update your version')
checkVersion([1, 17, 3, 42480])
import chimera
from chimera import replyobj
replyobj.status('Restoring session...', \
    blankAfter=0)
replyobj.status('Beginning session restore...', \
    blankAfter=0, secondary=True)
beginRestore()

def restoreCoreModels():
	from SimpleSession.versions.v65 import init, restoreViewer, \
	     restoreMolecules, restoreColors, restoreSurfaces, \
	     restoreVRML, restorePseudoBondGroups, restoreModelAssociations
	molInfo = cPickle.loads(base64.b64decode('gAJ9cQEoVRFyaWJib25JbnNpZGVDb2xvcnECSwFOfYdVCWJhbGxTY2FsZXEDSwFHP9AAAAAAAAB9h1UJcG9pbnRTaXplcQRLAUc/8AAAAAAAAH2HVQVjb2xvcnEFSwFLAH2HVQpyaWJib25UeXBlcQZLAUsAfYdVCnN0aWNrU2NhbGVxB0sBRz/wAAAAAAAAfYdVDG1tQ0lGSGVhZGVyc3EIXXEJTmFVDGFyb21hdGljTW9kZXEKSwFLAX2HVQp2ZHdEZW5zaXR5cQtLAUdAFAAAAAAAAH2HVQZoaWRkZW5xDEsBiX2HVQ1hcm9tYXRpY0NvbG9ycQ1LAU59h1UPcmliYm9uU21vb3RoaW5ncQ5LAUsAfYdVCWF1dG9jaGFpbnEPSwGIfYdVCnBkYlZlcnNpb25xEEsBSwB9h1UIb3B0aW9uYWxxEX1xElUIb3BlbmVkQXNxE4iJSwEoVUIvVXNlcnMvc2VyZ2lvcnRpenJvcGVyby9URkdfcGh5cy9OTlBzX1RGRy9leGFtcGxlcy9DT1NBTi9jb3Nhbi54eXpOTksBdHEUfYeHc1UPbG93ZXJDYXNlQ2hhaW5zcRVLAYl9h1UJbGluZVdpZHRocRZLAUc/8AAAAAAAAH2HVQ9yZXNpZHVlTGFiZWxQb3NxF0sBSwB9h1UEbmFtZXEYSwFYEAAAAGdlbmVyYXRlZCBieSBWTUR9h1UPYXJvbWF0aWNEaXNwbGF5cRlLAYl9h1UPcmliYm9uU3RpZmZuZXNzcRpLAUc/6ZmZmZmZmn2HVQpwZGJIZWFkZXJzcRtdcRx9cR1hVQNpZHNxHksBSwBLAIZ9h1UOc3VyZmFjZU9wYWNpdHlxH0sBR7/wAAAAAAAAfYdVEGFyb21hdGljTGluZVR5cGVxIEsBSwJ9h1UUcmliYm9uSGlkZXNNYWluY2hhaW5xIUsBiH2HVQdkaXNwbGF5cSJLAYh9h3Uu'))
	resInfo = cPickle.loads(base64.b64decode('gAJ9cQEoVQZpbnNlcnRxAksBVQEgfYdVC2ZpbGxEaXNwbGF5cQNLAYl9h1UEbmFtZXEESwFYAwAAAFVOS32HVQVjaGFpbnEFSwFYAQAAACB9h1UOcmliYm9uRHJhd01vZGVxBksBSwJ9h1UCc3NxB0sBiYmGfYdVCG1vbGVjdWxlcQhLAUsAfYdVC3JpYmJvbkNvbG9ycQlLAU59h1UFbGFiZWxxCksBWAAAAAB9h1UKbGFiZWxDb2xvcnELSwFOfYdVCGZpbGxNb2RlcQxLAUsBfYdVBWlzSGV0cQ1LAYl9h1ULbGFiZWxPZmZzZXRxDksBTn2HVQhwb3NpdGlvbnEPXXEQSwFLAYZxEWFVDXJpYmJvbkRpc3BsYXlxEksBiX2HVQhvcHRpb25hbHETfVUEc3NJZHEUSwFK/////32HdS4='))
	atomInfo = cPickle.loads(base64.b64decode('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'))
	bondInfo = cPickle.loads(base64.b64decode('gAJ9cQEoVQVjb2xvcnECS0hOfYdVBWF0b21zcQNdcQQoXXEFKEsCSwNlXXEGKEsCSwdlXXEHKEsCSwhlXXEIKEsCSwllXXEJKEsCSxllXXEKKEsDSwRlXXELKEsDSwZlXXEMKEsDSwdlXXENKEsDSwllXXEOKEsDSxplXXEPKEsESwVlXXEQKEsESwZlXXERKEsESwllXXESKEsESwplXXETKEsESxtlXXEUKEsFSwZlXXEVKEsFSwplXXEWKEsFSwtlXXEXKEsFSwxlXXEYKEsFSxxlXXEZKEsGSwdlXXEaKEsGSwxlXXEbKEsGSx1lXXEcKEsHSwhlXXEdKEsHSwxlXXEeKEsHSx5lXXEfKEsISwtlXXEgKEsISwxlXXEhKEsISx9lXXEiKEsJSwplXXEjKEsJSyBlXXEkKEsKSwtlXXElKEsKSyFlXXEmKEsLSwxlXXEnKEsLSyJlXXEoKEsMSyNlXXEpKEsNSw5lXXEqKEsNSxJlXXErKEsNSxNlXXEsKEsNSxRlXXEtKEsNSyRlXXEuKEsOSw9lXXEvKEsOSxFlXXEwKEsOSxJlXXExKEsOSxRlXXEyKEsOSyVlXXEzKEsPSxBlXXE0KEsPSxFlXXE1KEsPSxRlXXE2KEsPSxVlXXE3KEsPSyZlXXE4KEsQSxFlXXE5KEsQSxVlXXE6KEsQSxZlXXE7KEsQSxdlXXE8KEsQSydlXXE9KEsRSxJlXXE+KEsRSxdlXXE/KEsRSyhlXXFAKEsSSxNlXXFBKEsSSxdlXXFCKEsSSyllXXFDKEsTSxZlXXFEKEsTSxdlXXFFKEsTSyplXXFGKEsUSxVlXXFHKEsUSytlXXFIKEsVSxZlXXFJKEsVSyxlXXFKKEsWSxdlXXFLKEsWSy1lXXFMKEsXSy5lZVUFbGFiZWxxTUtIWAAAAAB9h1UIaGFsZmJvbmRxTktIiH2HVQZyYWRpdXNxT0tIRz3bfN/gAAAAfYdVC2xhYmVsT2Zmc2V0cVBLSE59h1UIZHJhd01vZGVxUUtISwF9h1UIb3B0aW9uYWxxUn1VB2Rpc3BsYXlxU0tISwJ9h3Uu'))
	crdInfo = cPickle.loads(base64.b64decode('gAJ9cQFLAH1xAihLAF1xAyhHP9ffO2RaHKxHP/YxJul41P5HP/jdLxqfvneHcQRHv91P3ztkWh1HP/fjU/fO2RdHQAhHrhR64UiHcQVHv/T1wo9cKPZHv687ZFocrAhHQAko9cKPXCmHcQZHv7R64UeuFHtHv/WuFHrhR65HQAkxJul41P6HcQdHP88an752yLRHP8fvnbItDlZHQBAYk3S8an+HcQhHP/SHKwIMSbpHP/KwIMSbpeNHQAfpeNT987aHcQlHP/eZmZmZmZpHP84UeuFHrhRHP/kGJN0vGqCHcQpHv/MzMzMzMzNHP+ij1wo9cKRHP/lDlYEGJN2HcQtHv++uFHrhR65Hv+/vnbItDlZHP/otDlYEGJOHcQxHP+jtkWhysCFHv/TAgxJul41HP/lwo9cKPXGHcQ1HP/haHKwIMSdHv+KwIMSbpeNHQAhocrAgxJyHcQ5HP/JJul41P31HP+2RaHKwIMVHv/jZFocrAgyHcQ9HP/pBiTdLxqhHP841P3ztkWhHwAg9cKPXCj2HcRBHP+ZeNT987ZFHv/RN0vGp++dHwAkIMSbpeNWHcRFHv/BysCDEm6ZHv+p++dsi0OVHwAkan752yLSHcRJHP8TdLxqfvndHP8l41P3ztkZHwBAUeuFHrhSHcRNHP+BBiTdLxqhHP/mNT987ZFpHwAf52yLQ5WCHcRRHv9mZmZmZmZpHP/UrAgxJul5Hv/kWhysCDEqHcRVHP/XbItDlYEJHv+f3ztkWhytHv/kan752yLSHcRZHv9GZmZmZmZpHv/btkWhysCFHv/nXCj1wo9eHcRdHv/ZFocrAgxJHv6FocrAgxJxHv/locrAgxJyHcRhHv/ItDlYEGJNHP+5N0vGp++dHwAhysCDEm6aHcRlHAAAAAAAAAABHAAAAAAAAAABHAAAAAAAAAACHcRpHP+TEm6XjU/hHQAKdsi0OVgRHP/ESbpeNT9+HcRtHv+o1P3ztkWhHQARul41P3ztHQAtaHKwIMSeHcRxHwAK+dsi0OVhHv8O2RaHKwINHQA3dLxqfvneHcR1Hv81P3ztkWh1HwAMMSbpeNT9HQA3jU/fO2ReHcR5HP9RJul41P31HP9EGJN0vGqBHQBTT987ZFoeHcR9HQADjU/fO2RdHP/9ocrAgxJxHQAocrAgxJumHcSBHQANsi0OVgQZHP90/fO2RaHNHP/EzMzMzMzOHcSFHwACl41P3ztlHP/Z2yLQ5WBBHP/GZmZmZmZqHcSJHv/zxqfvnbItHv/yXjU/fO2RHP/Rul41P3zuHcSNHP/W6XjU/fO5HwAHKwIMSbphHP/IYk3S8an+HcSRHQAR2yLQ5WBBHv+/vnbItDlZHQAudsi0OVgSHcSVHP/1HrhR64UhHP/oAAAAAAABHv/Ean752yLSHcSZHQAX1wo9cKPZHP9vGp++dsi1HwAtN0vGp++eHcSdHP/IIMSbpeNVHwAHEm6XjU/hHwA2j1wo9cKSHcShHv/2hysCDEm9Hv/dgQYk3S8dHwA3Em6XjU/iHcSlHP8j1wo9cKPZHP9KwIMSbpeNHwBTR64UeuFKHcSpHP+mBBiTdLxtHQAWj1wo9cKRHwApDlYEGJN2HcStHv+WRaHKwIMVHQAIi0OVgQYlHv/Fwo9cKPXGHcSxHQALItDlYEGJHv/M3S8an755Hv/FP3ztkWh2HcS1Hv+HS8an7521HwAQ/fO2RaHNHv/PztkWhysGHcS5HwAPlYEGJN0xHP5ul41P3ztlHv/I1P3ztkWiHcS9HwAAIMSbpeNVHP/pN0vGp++dHwAuyLQ5WBBmHcTBlVQZhY3RpdmVxMUsAdXMu'))
	surfInfo = {'category': (0, None, {}), 'probeRadius': (0, None, {}), 'pointSize': (0, None, {}), 'name': [], 'density': (0, None, {}), 'colorMode': (0, None, {}), 'useLighting': (0, None, {}), 'transparencyBlendMode': (0, None, {}), 'molecule': [], 'smoothLines': (0, None, {}), 'lineWidth': (0, None, {}), 'allComponents': (0, None, {}), 'twoSidedLighting': (0, None, {}), 'customVisibility': [], 'drawMode': (0, None, {}), 'display': (0, None, {}), 'customColors': []}
	vrmlInfo = {'subid': (0, None, {}), 'display': (0, None, {}), 'id': (0, None, {}), 'vrmlString': [], 'name': (0, None, {})}
	colors = {u'': ((0, 0.670588, 0.141176), 1, u''), u'Ru': ((0.141176, 0.560784, 0.560784), 1, u'default'), u'Re': ((0.14902, 0.490196, 0.670588), 1, u'default'), u'Rf': ((0.8, 0, 0.34902), 1, u'default'), u'Ra': ((0, 0.490196, 0), 1, u'default'), u'Rb': ((0.439216, 0.180392, 0.690196), 1, u'default'), u'Rn': ((0.258824, 0.509804, 0.588235), 1, u'default'), u'Rh': ((0.0392157, 0.490196, 0.54902), 1, u'default'), u'Be': ((0.760784, 1, 0), 1, u'default'), u'Ba': ((0, 0.788235, 0), 1, u'default'), u'Bh': ((0.878431, 0, 0.219608), 1, u'default'), u'Bi': ((0.619608, 0.309804, 0.709804), 1, u'default'), u'Bk': ((0.541176, 0.309804, 0.890196), 1, u'default'), u'Br': ((0.65098, 0.160784, 0.160784), 1, u'default'), u'H': ((1, 1, 1), 1, u'default'), u'P': ((1, 0.501961, 0), 1, u'default'), u'Os': ((0.14902, 0.4, 0.588235), 1, u'default'), u'Es': ((0.701961, 0.121569, 0.831373), 1, u'default'), u'Hg': ((0.721569, 0.721569, 0.815686), 1, u'default'), u'Ge': ((0.4, 0.560784, 0.560784), 1, u'default'), u'Gd': ((0.270588, 1, 0.780392), 1, u'default'), u'Ga': ((0.760784, 0.560784, 0.560784), 1, u'default'),
u'Pr': ((0.85098, 1, 0.780392), 1, u'default'), u'Pt': ((0.815686, 0.815686, 0.878431), 1, u'default'), u'Pu': ((0, 0.419608, 1), 1, u'default'), u'C': ((0.564706, 0.564706, 0.564706), 1, u'default'), u'Pb': ((0.341176, 0.34902, 0.380392), 1, u'default'), u'Pa': ((0, 0.631373, 1), 1, u'default'), u'Pd': ((0, 0.411765, 0.521569), 1, u'default'), u'Xe': ((0.258824, 0.619608, 0.690196), 1, u'default'), u'Po': ((0.670588, 0.360784, 0), 1, u'default'), u'Pm': ((0.639216, 1, 0.780392), 1, u'default'), u'Hs': ((0.901961, 0, 0.180392), 1, u'default'), u'Ho': ((0, 1, 0.611765), 1, u'default'), u'Hf': ((0.301961, 0.760784, 1), 1, u'default'), u'Mo': ((0.329412, 0.709804, 0.709804), 1, u'default'), u'He': ((0.85098, 1, 1), 1, u'default'), u'Md': ((0.701961, 0.0509804, 0.65098), 1, u'default'), u'Mg': ((0.541176, 1, 0), 1, u'default'), u'K': ((0.560784, 0.25098, 0.831373), 1, u'default'), u'Mn': ((0.611765, 0.478431, 0.780392), 1, u'default'), u'O': ((1, 0.0509804, 0.0509804), 1, u'default'), u'Mt': ((0.921569, 0, 0.14902), 1, u'default'), u'S': ((1, 1, 0.188235), 1, u'default'),
u'W': ((0.129412, 0.580392, 0.839216), 1, u'default'), u'Zn': ((0.490196, 0.501961, 0.690196), 1, u'default'), u'Eu': ((0.380392, 1, 0.780392), 1, u'default'), u'Zr': ((0.580392, 0.878431, 0.878431), 1, u'default'), u'Er': ((0, 0.901961, 0.458824), 1, u'default'), u'Ni': ((0.313725, 0.815686, 0.313725), 1, u'default'), u'No': ((0.741176, 0.0509804, 0.529412), 1, u'default'), u'Na': ((0.670588, 0.360784, 0.94902), 1, u'default'), u'Nb': ((0.45098, 0.760784, 0.788235), 1, u'default'), u'Nd': ((0.780392, 1, 0.780392), 1, u'default'), u'Ne': ((0.701961, 0.890196, 0.960784), 1, u'default'), u'Np': ((0, 0.501961, 1), 1, u'default'), u'Fr': ((0.258824, 0, 0.4), 1, u'default'), u'Fe': ((0.878431, 0.4, 0.2), 1, u'default'), u'Fm': ((0.701961, 0.121569, 0.729412), 1, u'default'), u'B': ((1, 0.709804, 0.709804), 1, u'default'), u'F': ((0.564706, 0.878431, 0.313725), 1, u'default'), u'Sr': ((0, 1, 0), 1, u'default'), u'N': ((0.188235, 0.313725, 0.972549), 1, u'default'), u'Kr': ((0.360784, 0.721569, 0.819608), 1, u'default'), u'Si': ((0.941176, 0.784314, 0.627451), 1, u'default'),
u'Sn': ((0.4, 0.501961, 0.501961), 1, u'default'), u'Sm': ((0.560784, 1, 0.780392), 1, u'default'), u'V': ((0.65098, 0.65098, 0.670588), 1, u'default'), u'Sc': ((0.901961, 0.901961, 0.901961), 1, u'default'), u'Sb': ((0.619608, 0.388235, 0.709804), 1, u'default'), u'Sg': ((0.85098, 0, 0.270588), 1, u'default'), u'Se': ((1, 0.631373, 0), 1, u'default'), u'Co': ((0.941176, 0.564706, 0.627451), 1, u'default'), u'Cm': ((0.470588, 0.360784, 0.890196), 1, u'default'), u'Cl': ((0.121569, 0.941176, 0.121569), 1, u'default'), u'Ca': ((0.239216, 1, 0), 1, u'default'), u'Cf': ((0.631373, 0.211765, 0.831373), 1, u'default'), u'Ce': ((1, 1, 0.780392), 1, u'default'), u'Cd': ((1, 0.85098, 0.560784), 1, u'default'), u'Lu': ((0, 0.670588, 0.141176), 1, u'default'), u'Cs': ((0.341176, 0.0901961, 0.560784), 1, u'default'), u'Cr': ((0.541176, 0.6, 0.780392), 1, u'default'), u'Cu': ((0.784314, 0.501961, 0.2), 1, u'default'), u'La': ((0.439216, 0.831373, 1), 1, u'default'), u'Li': ((0.8, 0.501961, 1), 1, u'default'), u'Tl': ((0.65098, 0.329412, 0.301961), 1, u'default'),
u'Tm': ((0, 0.831373, 0.321569), 1, u'default'), u'Lr': ((0.780392, 0, 0.4), 1, u'default'), u'Th': ((0, 0.729412, 1), 1, u'default'), u'Ti': ((0.74902, 0.760784, 0.780392), 1, u'default'), u'tan': ((0.823529, 0.705882, 0.54902), 1, u'default'), u'Te': ((0.831373, 0.478431, 0), 1, u'default'), u'Tb': ((0.188235, 1, 0.780392), 1, u'default'), u'Tc': ((0.231373, 0.619608, 0.619608), 1, u'default'), u'Ta': ((0.301961, 0.65098, 1), 1, u'default'), u'Yb': ((0, 0.74902, 0.219608), 1, u'default'), u'Db': ((0.819608, 0, 0.309804), 1, u'default'), u'Dy': ((0.121569, 1, 0.780392), 1, u'default'), u'I': ((0.580392, 0, 0.580392), 1, u'default'), u'medium purple': ((0.576471, 0.439216, 0.858824), 1, u'default'), u'U': ((0, 0.560784, 1), 1, u'default'), u'Y': ((0.580392, 1, 1), 1, u'default'), u'Ac': ((0.439216, 0.670588, 0.980392), 1, u'default'), u'Ag': ((0.752941, 0.752941, 0.752941), 1, u'default'), u'Ir': ((0.0901961, 0.329412, 0.529412), 1, u'default'), u'Am': ((0.329412, 0.360784, 0.94902), 1, u'default'), u'Al': ((0.74902, 0.65098, 0.65098), 1, u'default'),
u'As': ((0.741176, 0.501961, 0.890196), 1, u'default'), u'Ar': ((0.501961, 0.819608, 0.890196), 1, u'default'), u'Au': ((1, 0.819608, 0.137255), 1, u'default'), u'At': ((0.458824, 0.309804, 0.270588), 1, u'default'), u'In': ((0.65098, 0.458824, 0.45098), 1, u'default')}
	materials = {u'': ((0.85, 0.85, 0.85), 30), u'default': ((0.85, 0.85, 0.85), 30)}
	pbInfo = {'category': [u'coordination complexes of generated by VMD (#0)', u'distance monitor'], 'bondInfo': [{'color': (10, 46, {}), 'atoms': [[24, 11], [24, 13], [24, 8], [24, 9], [24, 10], [24, 19], [24, 20], [24, 21], [24, 22], [24, 2]], 'label': (10, u'', {}), 'halfbond': (10, False, {}), 'labelColor': (10, None, {}), 'labelOffset': (10, chimera.Vector(-1e+99, 0.0, 0.0), {chimera.Vector(-1e+99, 0.0, 0.0): [0], chimera.Vector(-1e+99, 0.0, 0.0): [7], chimera.Vector(-1e+99, 0.0, 0.0): [1], chimera.Vector(-1e+99, 0.0, 0.0): [2], chimera.Vector(-1e+99, 0.0, 0.0): [4], chimera.Vector(-1e+99, 0.0, 0.0): [9], chimera.Vector(-1e+99, 0.0, 0.0): [8], chimera.Vector(-1e+99, 0.0, 0.0): [5], chimera.Vector(-1e+99, 0.0, 0.0): [3]}), 'drawMode': (10, 0, {}), 'display': (10, 2, {})}, {'color': (0, None, {}), 'atoms': [], 'label': (0, None, {}), 'halfbond': (0, None, {}), 'labelColor': (0, None, {}), 'labelOffset': (0, None, {}), 'drawMode': (0, None, {}), 'display': (0, None, {})}], 'lineType': (2, 2, {}), 'color': (2, 44, {45: [1]}), 'optional': {'fixedLabels': (True, False, (2, False, {None: [0]}))},
'display': (2, True, {}), 'showStubBonds': (2, False, {}), 'lineWidth': (2, 1, {2: [0]}), 'stickScale': (2, 1, {}), 'id': [0, -2]}
	modelAssociations = {0: [129]}
	colorInfo = (49, (u'', (1, 1, 1, 0.1)), {(u'green', (0, 1, 0, 1)): [48], (u'', (0.538462, 0.564706, 0.627451, 1)): [21], (u'', (1, 0.709804, 0.709804, 0.1)): [2, 3, 4, 5, 6, 11, 13, 14, 15, 16, 17, 20], (u'medium purple', (0.576471, 0.439216, 0.858824, 1)): [44], (u'', (1, 0.709804, 0.709804, 1)): [8, 9, 10, 19], (u'tan', (0.823529, 0.705882, 0.54902, 1)): [0], (u'', (0.653846, 0.653846, 0.653846, 1)): [12, 18], (u'yellow', (1, 1, 0, 1)): [45], (u'', (0.653849, 0.653849, 0.653849, 1)): [1, 7], (u'', (0.192308, 0, 0.846154, 1)): [46], (u'white', (1, 1, 1, 1)): [47], (u'', (1, 1, 1, 0.0769231)): [31]})
	viewerInfo = {'cameraAttrs': {'center': (0.129, 0.087, 0.21169805325909), 'fieldOfView': 13.20890159592, 'nearFar': (6.5986142011766, -13.944066894392), 'ortho': False, 'eyeSeparation': 50.8, 'focal': 0.00099999999999945}, 'viewerAttrs': {'silhouetteColor': None, 'clipping': True, 'showSilhouette': False, 'showShadows': False, 'viewSize': 7.9563832979382, 'labelsOnTop': True, 'depthCueRange': (0.5, 1), 'silhouetteWidth': 2, 'singleLayerTransparency': True, 'shadowTextureSize': 2048, 'backgroundImage': [None, 1, 2, 1, 0, 0], 'backgroundGradient': [('Chimera default', [(1, 1, 1, 1), (0, 0, 1, 1)], 1), 1, 0, 0], 'depthCue': True, 'highlight': 0, 'scaleFactor': 1.35282055607, 'angleDependentTransparency': True, 'backgroundMethod': 0}, 'viewerHL': 48, 'cameraMode': 'mono', 'detail': 5, 'viewerFog': None, 'viewerBG': 47}

	replyobj.status("Initializing session restore...", blankAfter=0,
		secondary=True)
	from SimpleSession.versions.v65 import expandSummary
	init(dict(enumerate(expandSummary(colorInfo))))
	replyobj.status("Restoring colors...", blankAfter=0,
		secondary=True)
	restoreColors(colors, materials)
	replyobj.status("Restoring molecules...", blankAfter=0,
		secondary=True)
	restoreMolecules(molInfo, resInfo, atomInfo, bondInfo, crdInfo)
	replyobj.status("Restoring surfaces...", blankAfter=0,
		secondary=True)
	restoreSurfaces(surfInfo)
	replyobj.status("Restoring VRML models...", blankAfter=0,
		secondary=True)
	restoreVRML(vrmlInfo)
	replyobj.status("Restoring pseudobond groups...", blankAfter=0,
		secondary=True)
	restorePseudoBondGroups(pbInfo)
	replyobj.status("Restoring model associations...", blankAfter=0,
		secondary=True)
	restoreModelAssociations(modelAssociations)
	replyobj.status("Restoring camera...", blankAfter=0,
		secondary=True)
	restoreViewer(viewerInfo)

try:
	restoreCoreModels()
except:
	reportRestoreError("Error restoring core models")

	replyobj.status("Restoring extension info...", blankAfter=0,
		secondary=True)


try:
	import StructMeasure
	from StructMeasure.DistMonitor import restoreDistances
	registerAfterModelsCB(restoreDistances, 1)
except:
	reportRestoreError("Error restoring distances in session")


def restoreMidasBase():
	formattedPositions = {'session-start': (0.81051558821553, 7.9613052474936, (0.129, 0.087, 0.09029385111756), (6.5986142011766, -13.944066894392), 0.00099999999999945, {(0, 0): ((0.056482898151216, 0.063883786671822, -0.055491147755838), (0.9133239842353392, -0.3060360704182698, 0.26866563498785984, 99.75498798311399))}, {(0, 0, 'Molecule'): (False, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, False, 5.0)}, 4, (0.1089766431812973, 0.049666162531389446, 0.09029385111756572), True, 13.20890159592)}
	import Midas
	Midas.restoreMidasBase(formattedPositions)
try:
	restoreMidasBase()
except:
	reportRestoreError('Error restoring Midas base state')


def restoreMidasText():
	from Midas import midas_text
	midas_text.aliases = {}
	midas_text.userSurfCategories = {}

try:
	restoreMidasText()
except:
	reportRestoreError('Error restoring Midas text state')


def restore_cap_attributes():
 cap_attributes = \
  {
   'cap_attributes': [ ],
   'cap_color': None,
   'cap_offset': 0.01,
   'class': 'Caps_State',
   'default_cap_offset': 0.01,
   'mesh_style': False,
   'shown': True,
   'subdivision_factor': 1.0,
   'version': 1,
  }
 import SurfaceCap.session
 SurfaceCap.session.restore_cap_attributes(cap_attributes)
registerAfterModelsCB(restore_cap_attributes)


def restore_volume_data():
 volume_data_state = \
  {
   'class': 'Volume_Manager_State',
   'data_and_regions_state': [ ],
   'version': 2,
  }
 from VolumeViewer import session
 session.restore_volume_data_state(volume_data_state)

try:
  restore_volume_data()
except:
  reportRestoreError('Error restoring volume data')

geomData = {'AxisManager': {}, 'CentroidManager': {}, 'PlaneManager': {}}

try:
	from StructMeasure.Geometry import geomManager
	geomManager._restoreSession(geomData)
except:
	reportRestoreError("Error restoring geometry objects in session")


def restoreSession_RibbonStyleEditor():
	import SimpleSession
	import RibbonStyleEditor
	userScalings = [('licorice', [[0.35, 0.35], [0.35, 0.35], [0.35, 0.35], [0.35, 0.35, 0.35, 0.35], [0.35, 0.35]])]
	userXSections = []
	userResidueClasses = []
	residueData = [(1, 'Chimera default', 'rounded', u'unknown')]
	flags = RibbonStyleEditor.NucleicDefault1
	SimpleSession.registerAfterModelsCB(RibbonStyleEditor.restoreState,
				(userScalings, userXSections,
				userResidueClasses, residueData, flags))
try:
	restoreSession_RibbonStyleEditor()
except:
	reportRestoreError("Error restoring RibbonStyleEditor state")

trPickle = 'gAJjQW5pbWF0ZS5UcmFuc2l0aW9ucwpUcmFuc2l0aW9ucwpxASmBcQJ9cQMoVQxjdXN0b21fc2NlbmVxBGNBbmltYXRlLlRyYW5zaXRpb24KVHJhbnNpdGlvbgpxBSmBcQZ9cQcoVQZmcmFtZXNxCEsBVQ1kaXNjcmV0ZUZyYW1lcQlLAVUKcHJvcGVydGllc3EKXXELVQNhbGxxDGFVBG5hbWVxDVUMY3VzdG9tX3NjZW5lcQ5VBG1vZGVxD1UGbGluZWFycRB1YlUIa2V5ZnJhbWVxEWgFKYFxEn1xEyhoCEsUaAlLAWgKXXEUaAxhaA1VCGtleWZyYW1lcRVoD2gQdWJVBXNjZW5lcRZoBSmBcRd9cRgoaAhLAWgJSwFoCl1xGWgMYWgNVQVzY2VuZXEaaA9oEHVidWIu'
scPickle = 'gAJjQW5pbWF0ZS5TY2VuZXMKU2NlbmVzCnEBKYFxAn1xA1UHbWFwX2lkc3EEfXNiLg=='
kfPickle = 'gAJjQW5pbWF0ZS5LZXlmcmFtZXMKS2V5ZnJhbWVzCnEBKYFxAn1xA1UHZW50cmllc3EEXXEFc2Iu'
def restoreAnimation():
	'A method to unpickle and restore animation objects'
	# Scenes must be unpickled after restoring transitions, because each
	# scene links to a 'scene' transition. Likewise, keyframes must be 
	# unpickled after restoring scenes, because each keyframe links to a scene.
	# The unpickle process is left to the restore* functions, it's 
	# important that it doesn't happen prior to calling those functions.
	import SimpleSession
	from Animate.Session import restoreTransitions
	from Animate.Session import restoreScenes
	from Animate.Session import restoreKeyframes
	SimpleSession.registerAfterModelsCB(restoreTransitions, trPickle)
	SimpleSession.registerAfterModelsCB(restoreScenes, scPickle)
	SimpleSession.registerAfterModelsCB(restoreKeyframes, kfPickle)
try:
	restoreAnimation()
except:
	reportRestoreError('Error in Animate.Session')

def restoreLightController():
	import Lighting
	Lighting._setFromParams({'ratio': 1.25, 'brightness': 1.16, 'material': [30.0, (0.85, 0.85, 0.85), 1.0], 'back': [(0.3574067443365933, 0.6604015517481455, -0.6604015517481456), (1.0, 1.0, 1.0), 0.0], 'mode': 'two-point', 'key': [(-0.3574067443365933, 0.6604015517481455, 0.6604015517481456), (1.0, 1.0, 1.0), 1.0], 'contrast': 0.83, 'fill': [(0.2505628070857316, 0.2505628070857316, 0.9351131265310294), (1.0, 1.0, 1.0), 0.0]})
try:
	restoreLightController()
except:
	reportRestoreError("Error restoring lighting parameters")


def restoreRemainder():
	from SimpleSession.versions.v65 import restoreWindowSize, \
	     restoreOpenStates, restoreSelections, restoreFontInfo, \
	     restoreOpenModelsAttrs, restoreModelClip, restoreSilhouettes

	curSelIds =  []
	savedSels = []
	openModelsAttrs = { 'cofrMethod': 4 }
	windowSize = (1534, 1606)
	xformMap = {0: (((0.18168102684352, -0.80501722653146, 0.56474708451897), 163.47291937532), (0.033587818655092, -0.029760123897943, 0.22954114544876), True)}
	fontInfo = {'face': (u'Sans Serif', u'Bold', 36)}
	clipPlaneInfo = {}
	silhouettes = {0: True, 129: True, 130: True}

	replyobj.status("Restoring window...", blankAfter=0,
		secondary=True)
	restoreWindowSize(windowSize)
	replyobj.status("Restoring open states...", blankAfter=0,
		secondary=True)
	restoreOpenStates(xformMap)
	replyobj.status("Restoring font info...", blankAfter=0,
		secondary=True)
	restoreFontInfo(fontInfo)
	replyobj.status("Restoring selections...", blankAfter=0,
		secondary=True)
	restoreSelections(curSelIds, savedSels)
	replyobj.status("Restoring openModel attributes...", blankAfter=0,
		secondary=True)
	restoreOpenModelsAttrs(openModelsAttrs)
	replyobj.status("Restoring model clipping...", blankAfter=0,
		secondary=True)
	restoreModelClip(clipPlaneInfo)
	replyobj.status("Restoring per-model silhouettes...", blankAfter=0,
		secondary=True)
	restoreSilhouettes(silhouettes)

	replyobj.status("Restoring remaining extension info...", blankAfter=0,
		secondary=True)
try:
	restoreRemainder()
except:
	reportRestoreError("Error restoring post-model state")
from SimpleSession.versions.v65 import makeAfterModelsCBs
makeAfterModelsCBs()

from SimpleSession.versions.v65 import endRestore
replyobj.status('Finishing restore...', blankAfter=0, secondary=True)
endRestore({})
replyobj.status('', secondary=True)
replyobj.status('Restore finished.')

