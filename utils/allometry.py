import numpy as np
from pygbif import species

DIAMETER_THRESHOLD = 10

def get_biomass(name, diameter):
    # genus, species
    genus, s = name.lower().split()[:2]
    family, spg = None, None
    try:
        family, spg = get_taxa_family_spg(genus, s)
    except TypeError:
        try:
            family, spg = get_taxa_family_spg(genus, 'sp.')
        except TypeError:
            pass
    if not family:
        family = species.name_backbone(name)['family']
        family = family.lower()
    b1, b2 = get_coeffs(family, spg)
    if b1 and b2:
        return cal_biomass(b1, b2, diameter)
    else:
        return np.nan

def cal_biomass(b1, b2, d):
    ln_biomass = b1 + b2*np.log(d)
    return np.exp(ln_biomass)

def get_coeffs(family, spg):
    if family == 'abies':
        if spg < 0.35:
            return -2.3123, 2.3482
        else:
            return -3.1774, 2.6426
    elif family == 'cupressaceae':
        if spg < 0.3:
            return -1.9615, 2.1063
        if 0.3 <= spg < 0.39:
            return -2.7765, 2.4195
        else:
            return -2.6327, 2.4757
    elif family == 'larix':
        return -2.3012, 2.3853
    elif family == 'picea':
        if spg < 0.35:
            return -3.0300, 2.5567
        else:
            return -2.1364, -2.3233
    elif family == 'pinus':
        if spg < 0.45:
            return -2.6177, 2.4638
        else:
            return -3.0506, 2.6465
    elif family == 'pseudotsuga':
        return -2.4623, 2.4852
    elif family == 'tsuga':
        if spg < 0.4:
            return -2.3480, 2.3876
        else:
            return -2.9208, 2.5697
    elif family == 'aceraceae':
        if spg < 0.5:
            return -2.0470, 2.3852
        else:
            return -1.8011, 2.3852
    elif family == 'betulaceae':
        if spg < 0.4:
            return -2.5932, 2.5349
        elif 0.40 <= spg <=0.49:
            return -2.2271, 2.4513
        elif 0.5 <= spg <= 0.59:
            return -1.8096, 2.3480
        else:
            return -2.2652, 2.5349
    elif family in ('cornaceae', 'ericaceae', 'lauraceae',
                    'platanaceae', 'rosaceae', 'ulmaceae'):
        return -2.2118, 2.4133
    elif family == 'juglandaceae':
        return -2.5095, 2.6175
    elif family == 'fabaceae':
        return -2.5095, 2.5437
    elif family == 'fagaceae_deciduous':
        return -2.0705, 2.4410
    elif family == 'fagaceae_evergreen':
        return -2.2198, 2.4410
    elif family == 'ceanothus_integerrimus':
        return 3.6672, 2.65018
    elif family == 'ribes_roezlii':
        return 3.761, 2.37498
    else:
        return None, None

def get_taxa_family_spg(genus, species):
    if genus == 'abies':
        if species in ('balsamea', 'fraseri', 'lasiocarpa'):
            return 'abies', 0.34
        elif species in ('amabilis', 'concolor', 'grandis', 'magnifica', 'procera', 'sp.'):
            return 'abies', 0.36

    elif genus == 'thuja':
        if species in ('occidentalis'):
            return 'cupressaceae', 0.29
    elif genus in ('calocedrus', 'sequoiadendron'):
        if species in ('decurrens', 'giganteum'):
            return 'cupressaceae', 0.35
    elif genus in ('chamaecyparis', 'juniperus'):
        if species in ('nookatensis', 'virginiana'):
            return 'cupressaceae', 0.41

    elif genus == 'larix':
        if species in ('laricina', 'occidentalis', 'sp.'):
            return 'larix', None
    
    elif genus == 'picea':
        if species in ('engelmannii', 'sitchensis'):
            return 'picea', 0.34
        if species in ('abies', 'glauca', 'mariana', 'rubens'):
            return 'picea', 0.36

    elif genus == 'pinus':
        if species in ('albicaulis', 'arizonica', 'banksiana','contorta', 'jeffreyi',
                    'lambertiana', 'leiophylla', 'monticola', 'ponderosa', 'resinosa',
                    'strobus', 'sp.'):
            return 'pinus', 0.44
        elif species in ('echinata', 'elliottii', 'palustris', 'rigida', 'taeda'):
            return 'pinus', 0.45
    
    elif genus == 'pseudotsuga':
        if species in 'menziesii':
            return 'pseudotsuga', None
    
    elif genus == 'tsuga':
        if species in ('canadensis'):
            return 'tsuga', 0.39
        elif species in ('heterophylla', 'mertensiana'):
            return 'tsuga', 0.4
    
    elif genus == 'acer':
        if species in ('macrophyllum', 'pensylvanicum', 'rubrum', 'saccharinum', 'spicatum'):
            return 'aceraceae', 0.49
        elif species in ('saccharum'):
            return 'aceraceae', 0.5
    
    elif genus == 'alnus':
        if species in ('rubra', 'sp.'):
            return 'betulaceae', 0.39
        elif species in ('papyrifera', 'populifolia'):
            return 'betulaceae', 0.45
        elif species in ('alleghaniensis'):
            return 'betulaceae', 0.55
        elif species in ('lenta'):
            return 'betulaceae', 0.6
    elif genus == 'ostrya':
        if species in ('virginiana'):
            return 'betulaceae', 0.6
    
    elif genus == 'cornus':
        if species in ('florida'):
            return 'cornaceae', None
    elif genus == 'nyssa':
        if species in ('aquatica', 'sylvatica'):
            return 'cornaceae', None
    elif genus == 'arbutus':
        if species in ('menziesii'):
            return 'ericaceae', None
    elif genus == 'oxydendrum':
        if species in ('arboreum'):
            return 'ericaceae', None
    elif genus == 'umbellularia':
        if species in ('californica'):
            return 'ericaceae', None
    elif genus == 'sassafras':
        if species in ('albidum'):
            return 'lauraceae', None
    elif genus == 'platanus':
        if species in ('occidentalis'):
            return 'platanaceae', None
    elif genus == 'amelanchier':
        if species in ('sp.'):
            return 'rosaceae', None
    elif genus == 'prunus':
        if species in ('pensylvanica', 'serotina', 'virginiana'):
            return 'rosaceae', None
    elif genus == 'sorbus':
        if species in ('americana'):
            return 'rosaceae', None
    elif genus == 'ulmus':
        if species in ('americana', 'sp.'):
            return 'ulmaceae', None

    elif genus == 'carya':
        if species in ('illinoinensis', 'ovata', 'sp.'):
            return 'juglandaceae', None
    
    elif genus == 'robinia':
        if species == 'pseudoacacia':
            return 'fabaceae', None

    elif genus == 'castanea':
        if species in ('dentata'):
            return 'fagaceae_deciduous', None
    elif genus == 'fagus':
        if species in ('grandifolia'):
            return 'fagaceae_deciduous', None
    elif genus == 'quercus':
        if species in ('alba', 'coccinea', 'ellipsoidalis', 'falcata',
                    'macrocarpa', 'nigra', 'prinus', 'rubra', 'stellata', 'velutina',
                    'sp.'):
            return 'fagaceae_deciduous', None
        elif species in ('douglasii', 'laurifolia', 'minima',
                        'chrysolepis'):
            return 'fagaceae_evergreen', None
    elif genus == 'chrysolepis':
        if species in ('chrysophylla'):
            return 'fagaceae_evergreen', None
    elif genus == 'lithocarpus':
        if species in ('densiflorus'):
            return 'fagaceae_evergreen', None

    # lulz
    elif genus == 'ceanothus':
        if species in ('integerrimus'):
            return 'ceanothus_integerrimus', None
    elif genus == 'ribes':
        if species in ('roezlii'):
            return 'ribes_roezlii', None
    else:
        return None, None
