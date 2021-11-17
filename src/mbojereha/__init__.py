# Mainumby. Parsing and translation with minimal dependency grammars.
#
########################################################################
#
#   This file is part of the Mainumby project within the PLoGS metaproject
#   for parsing, generation, translation, and computer-assisted
#   human translation.
#
#   Copyleft 2015, 2016, 2017, 2018, 2019 HLTDI, PLoGS <gasser@indiana.edu>
#
#   This program is free software: you can redistribute it and/or
#   modify it under the terms of the GNU General Public License as
#   published by the Free Software Foundation, either version 3 of
#   the License, or (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program. If not, see <http://www.gnu.org/licenses/>.
#
# =========================================================================

__all__ = ['language', 'entry', 'constraint', 'variable', 'sentence', 'cs', 'utils', 'record', 'train', 'tag']
#  not needed for now: 'learn', 'ui'

__version__ = '0.9'

## train imports sentence
from .train import *

## sentence imports ui, segment, individual classes from other modules
### segment imports cs, utils + individual classes
#### cs imports constraint
### ui imports language (ui itself not needed for current version)
#### language imports entry, some functions from utils, morphology.morpho, morphology.semiring
#### language also calls function in morphology.strip
##### entry imports morphology.fs, class and constant from morphology.semiring

## morphology a package; imports morphology.morpho
### which imports morphology.fst
#### which imports morphology.semiring
##### which imports morphology.fs, morphology.utils
###### fs imports morphology.logic, morphology.internals
from .morphology import *

# from .record import *

### Funciones que se llaman en views.py al realizar la interfaz.

# def start(gui, use_anon=True, create_memory=False):
#     """Iniciar una ejecución. Crear una sesión si hay un usuario y si no
#     se está usando una Memory."""
#     if not gui.source:
#         load(gui=gui)
#     # set GUI.user
#     if isinstance(gui.user, str):
#         # Get the user from their username
#         gui.user = get_human(gui.user)
#     if use_anon and not gui.user:
#         gui.user = get_human('anon')
#     username = ''
#     if gui.user:
#         username = gui.user.username
#     if create_memory:
#         gui.session = mbojereha.Memory.recreate(user=username)
#     elif gui.user:
#         gui.session = mbojereha.Session(source=gui.source, target=gui.target, user=gui.user)

def load(source='spa', target='grn', gui=None):
    """Cargar lenguas fuente y meta para traducción."""
    s, t = mbojereha.Language.load_trans(source, target)
    if gui:
        gui.source = s
        gui.target = t
    return s, t

def tra(oracion, source='spa', target='grn', html=False, user=None,
        choose=False, max_sols=3, verbosity=0):
    """
    Traducir oracion del source al target.
    """
    src, targ = load(mbojereha.Language.get_abbrev(source),
                     mbojereha.Language.get_abbrev(target))
#    print("** src {}, targ {}".format(src, targ))
    return oración(oracion, src=src, targ=targ,
                   user=user, max_sols=max_sols, translate=True,
                   connect=True, generate=True, html=html,
                   choose=False, verbosity=verbosity)

# def doc_sentences(doc=None, textobj=None, text='', textid=-1,
#                   gui=None, src=None, targ=None, user=None, verbosity=0):
#     """
#     Recopilar oraciones (instancias de Sentence) de una instancia
#     de Document o Text.
#     """
#     if not src and not targ:
#         if gui:
#             src = gui.source; targ = gui.target
#         else:
#             src, targ = Language.load_trans('spa', 'grn', bidir=False)
#     if doc:
#         return doc
#     else:
#         return sentences_from_text(textobj, textid, src, targ)

# def doc_trans(doc=None, textobj=None, text='', textid=-1, docpath='',
#               gui=None, src=None, targ=None, session=None, user=None,
#               terse=True):
#     """
#     Traducir todas las oraciones en un documento sin ofrecer opciones
#     al usuario. O doc es una instancia de Documento o textobj es una instancia
#     de Text o un Documento es creado con text como contenido."""
#     if not src and not targ:
#         if gui:
#             src = gui.source; targ = gui.target
#         else:
#             src, targ = Language.load_trans('spa', 'grn', bidir=False)
#     if not session:
#         session = make_session(src, targ, user, create_memory=True)
#     if not doc:
#         if docpath:
#             doc = Document(src, targ, path=docpath)
#     if doc:
#         sentences = doc
#     elif textid >= 0:
#         sentences = sentences_from_text(textobj, textid, src, targ)
#     elif text:
#         sentences = Document(src, targ, text=text)
#     if sentences:
#         translations = []
#         for sentence in sentences:
#             translation = oración(src=src, targ=targ, sentence=sentence, session=session,
#                                   html=False, choose=True, return_string=True,
#                                   verbosity=0, terse=terse)
#             translations.append(translation)
#         return translations
#     return []
#
## Creación y traducción de oración, dentro o fuera de la aplicación web

# def gui_trans(gui, session=None, choose=False, return_string=False,
#               sentence=None, terse=True, verbosity=0):
#     """
#     Traducir oración (accesible en gui) y devuelve la oración marcada (HTML) con
#     segmentos coloreados.
#     """
#     return oración(sentence=sentence or gui.sentence, src=gui.source,
#                    targ=gui.target, session=gui.session,
#                    html=True, return_string=return_string, choose=choose,
#                    verbosity=verbosity, terse=terse)

def oración(text='', src=None, targ=None, user=None, session=None,
            sentence=None, finalize=False, gui=False,
            max_sols=3, translate=True, connect=True, generate=True,
            html=False, choose=False,
            return_string=False, verbosity=0, terse=False):
    """
    Analizar y talvez también traducir una oración.
    """
    if not src and not targ:
        src, targ = Language.load_trans('spa', 'grn', bidir=False)
    if gui and not session:
        session = make_session(src, targ, user, create_memory=True)
    s = Sentence.solve_sentence(src, targ, text=text, session=session,
                                sentence=sentence,
                                max_sols=max_sols, choose=choose,
                                translate=translate,
                                verbosity=verbosity, terse=terse)
    segmentations = s.get_all_segmentations(translate=translate,
                                            generate=generate,
                                            agree_dflt=False, choose=choose,
                                            finalize=finalize,
                                            connect=connect, html=html,
                                            terse=terse)
    if choose:
        if segmentations:
            # there's already only one of these anyway
            segmentation = segmentations[0]
            # return the Segmentation
            if return_string:
                return segmentation.final
            else:
                return segmentation
        else:
            # no Segmentation; return the Sentence
            if return_string:
                return s.original
            else:
                return s
    elif html:
        if segmentations:
            segmentation = segmentations[0]
            return segmentation.segments, segmentation.get_segment_html()
        return [], s.get_html()
    elif segmentations:
        return segmentations
    return s

# def make_document(gui, text, html=False):
#     """
#     Create a Mainumby Document object with the source text, which
#     could be a word, sentence, or document.
#     """
#     print("CREATING NEW Document INSTANCE.")
#     session = gui.session
#     d = mbojereha.Document(gui.source, gui.target, text, proc=True, session=session)
#     if html:
#         d.set_html()
#     gui.doc = d
#     gui.init_doc()

# def quit(session=None):
#     """Quit the session (and the program), cleaning up in various ways."""
#     for language in Language.languages.values():
#         # Store new cached analyses or generated forms for
#         # each active language, but only if there is a current session/user.
#         language.quit(cache=session)
#     print("New items in session {} before committing: {}".format(db.session, db.session.new))
#     db.session.commit()
#
# def make_session(source, target, user, create_memory=False, use_anon=True):
#     """Create an instance of the Session or Memory class for the given user."""
#     User.read_all()
#     if isinstance(user, str):
#         # Get the user from their username
#         user = User.users.get(user)
#     if use_anon and not user:
#         user = User.get_anon()
#     username = ''
#     if user:
#         username = user.username
#     if create_memory:
#         session = mbojereha.Memory.recreate(user=username)
#     elif user:
#         session = mbojereha.Session(source=source, target=target, user=user)
#     return session

## DB functions

# def make_dbtext(content, language,
#                 name='', domain='Miscelánea', title='',
#                 description='', segment=False):
#     """
#     Create a Text database object with the given content and
#     language, returning its id.
#     """
#     text = Text(content=content, language=language,
#                 name=name, domain=domain, title=title,
#                 description=description, segment=segment)
#     return text
#
# def make_text(gui, textid):
#     """Initialize with the Text object specified by textid."""
#     textobj = get_text(textid)
#     nsent = len(textobj.segments)
#     html, html_list = get_doc_text_html(textobj)
#     gui.init_text(textid, nsent, html, html_list)
#
# def get_doc_text_html(text):
#     if not text.segments:
#         return
#     html = "<div id='doc'>"
#     seghtml = [s.html for s in text.segments]
#     html += ''.join(seghtml)
#     html += "</div>"
#     return html, seghtml
#
# def sentences_from_text(text=None, textid=-1, source=None, target=None):
#     """Get a list of sentences from the Text object."""
#     if not text and textid == -1:
#         return
#     text = text or get_text(textid)
#     sentences = []
#     for textseg in text.segments:
#         original = textseg.content
#         tokens = [tt.string for tt in textseg.tokens]
#         sentence = Sentence(original=original, tokens=tokens,
#                             language=source, target=target)
#         sentences.append(sentence)
#     return sentences
#
# def sentence_from_textseg(textseg=None, source=None, target=None, textid=None,
#                           oindex=-1):
#     """
#     Create a Sentence object from a DB TextSeg object, which is either
#     specified explicitly or accessed via its index within a Text object.
#     THERE'S SOME DUPLICATION HERE BECAUSE SENTENCE OBJECTS WERE ALREADY
#     CREATED WHEN THE Text OBJECT WAS CREATED IN THE DB.
#     """
# #    print("Creating sentence from textseg, source={}".format(source))
#     textseg = textseg or get_text(textid).segments[oindex]
#     original = textseg.content
#     tokens = [tt.string for tt in textseg.tokens]
#     return Sentence(original=original, tokens=tokens, language=source,
#                     target=target)

# def make_translation(text=None, textid=-1, accepted=None,
#                      translation='', user=None):
#     """
#     Create a Translation object, given a text, a user (translator), and a
#     list of sentence translations from the GUI. There may be missing
#     translations.
#     """
#     text = text or get_text(textid)
#     trans = Translation(text=text, translator=user)
#     db.session.add(trans)
#     sentences = accepted if any(accepted) else translation
#     # Sentence translations accepted separately
#     for index, sentence in enumerate(sentences):
#         if sentence:
#             ts = TraSeg(content=sentence, translation=trans, index=index)
#     print("Added translation {} to session {}".format(trans, db.session))
#     db.session.commit()
#     return trans
#
# def create_human(form):
#     """
#     Create and add to the text DB an instance of the Human class,
#     based on the form returned from tra.html.
#     """
#     level = form.get('level', 1)
#     level = int(level)
#     human = Human(username=form.get('username', ''),
#                   password=form.get('password'),
#                   email=form.get('email'),
#                   name=form.get('name', ''),
#                   level=level)
#     db.session.add(human)
#     db.session.commit()
#     return human
#
# def get_humans():
#     """Get all existing Human DB objects."""
#     return db.session.query(Human).all()
#
# def get_human(username):
#     """Get the Human DB object with the given username."""
#     humans = db.session.query(Human).filter_by(username=username).all()
#     if humans:
#         if len(humans) > 1:
#             print("Advertencia: ¡{} usuarios con el nombre de usuario {}!".format(len(humans), username))
#         return humans[0]
#
# def get_domains_texts():
#     """Return a list of domains and associated texts and a dict of texts by id."""
#     dom = dict([(d, []) for d in DOMAINS])
#     for text in db.session.query(Text).all():
#         d1 = text.domain
#         id = text.id
#         dom[d1].append((id, text.title))
#     # Alphabetize text titles
#     for texts in dom.values():
#         texts.sort(key=lambda x: x[1])
#     dom = list(dom.items())
#     # Alphabetize domain names
#     dom.sort()
#     return dom
#
# def get_text(id):
#     """Get the Text object with the given id."""
#     return db.session.query(Text).get(id)
