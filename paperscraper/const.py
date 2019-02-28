# URL
OAI = '{http://www.openarchives.org/OAI/2.0/}'
ARXIV = '{http://arxiv.org/OAI/arXiv/}'
META_BASE = 'http://export.arxiv.org/oai2?verb=ListRecords&'
E_PRINT_BASE = 'https://arxiv.org/e-print/'

# arXiv categories
CATS = [
    'astro-ph', 'cond-mat', 'gr-qc', 'hep-ex', 'hep-lat', 'hep-ph', 'hep-th',
    'math-ph', 'nlin', 'nucl-ex', 'nucl-th', 'physics', 'quant-ph', 'math', 'CoRR', 'q-bio',
    'q-fin', 'stat']
SUBCATS = {
    'cond-mat': [
        'cond-mat.dis-nn', 'cond-mat.mtrl-sci', 'cond-mat.mes-hall',
        'cond-mat.other', 'cond-mat.quant-gas', 'cond-mat.soft', 'cond-mat.stat-mech',
        'cond-mat.str-el', 'cond-mat.supr-con'],
    'hep-th': [],
    'hep-ex': [],
    'hep-ph': [],
    'gr-qc': [],
    'quant-ph': [],
    'q-fin': [
        'q-fin.CP', 'q-fin.EC', 'q-fin.GN', 'q-fin.MF', 'q-fin.PM',
        'q-fin.PR', 'q-fin.RM', 'q-fin.ST', 'q-fin.TR'],
    'nucl-ex': [],
    'CoRR': [],
    'nlin': ['nlin.AO', 'nlin.CG', 'nlin.CD', 'nlin.SI', 'nlin.PS'],
    'physics': [
        'physics.acc-ph', 'physics.app-ph', 'physics.ao-ph',
        'physics.atom-ph', 'physics.atm-clus', 'physics.bio-ph', 'physics.chem-ph',
        'physics.class-ph', 'physics.comp-ph', 'physics.data-an', 'physics.flu-dyn',
        'physics.gen-ph', 'physics.geo-ph', 'physics.hist-ph', 'physics.ins-det',
        'physics.med-ph', 'physics.optics', 'physics.ed-ph', 'physics.soc-ph',
        'physics.plasm-ph', 'physics.pop-ph', 'physics.space-ph'],
    'math-ph': [],
    'math': [
        'math.AG', 'math.AT', 'math.AP', 'math.CT', 'math.CA', 'math.CO',
        'math.AC', 'math.CV', 'math.DG', 'math.DS', 'math.FA', 'math.GM', 'math.GN',
        'math.GT', 'math.GR', 'math.HO', 'math.IT', 'math.KT', 'math.LO', 'math.MP',
        'math.MG', 'math.NT', 'math.NA', 'math.OA', 'math.OC', 'math.PR', 'math.QA',
        'math.RT', 'math.RA', 'math.SP', 'math.ST', 'math.SG'],
    'q-bio': [
        'q-bio.BM', 'q-bio.CB', 'q-bio.GN', 'q-bio.MN', 'q-bio.NC', 'q-bio.OT',
        'q-bio.PE', 'q-bio.QM', 'q-bio.SC', 'q-bio.TO'],
    'nucl-th': [],
    'stat': ['stat.AP', 'stat.CO', 'stat.ML','stat.ME', 'stat.OT', 'stat.TH'],
    'hep-lat': [],
    'astro-ph': ['astro-ph.GA','astro-ph.CO', 'astro-ph.EP', 'astro-ph.HE', 'astro-ph.IM', 'astro-ph.SR']
}

# Content-Type
TAR = 'application/x-eprint-tar'
PDF = 'application/pdf'