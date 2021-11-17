#!/usr/bin/env python3

# mbojereha: Parsing and translation between Spanish and Guarani
# with minimal dependency grammars.
#
#########################################################################
#
#   This file is part of the PLoGS project
#   for parsing, generation, translation, and computer-assisted
#   human translation.
#
#   Copyleft 2021. PLoGS <gasser@indiana.edu>
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
# 2021.11.11
# -- Created from mainumby, excluding the GUI and DB modules (and Flask, SQ

__version__ = 0.9

import mbojereha

## Creación y traducción de oración simple. Después de la segmentación inicial,
## se combinan los segmentos, usando patrones gramaticales ("joins") y grupos
## adicionales.

def tra(oracion, reverse=False, html=False, user=None, choose=False, verbosity=0):
    return ora(oracion, reverse=reverse, user=user, max_sols=2, translate=True,
               connect=True, generate=True, html=html, choose=choose,
               verbosity=verbosity)

## Creación (y opcionalmente traducción) de oración simple y de documento.

def ora(text, user=None, max_sols=2, translate=True, reverse=True,
        connect=True, generate=False, html=False, choose=False, verbosity=0):
    src, targ = cargar(reverse=reverse)
    return mbojereha.oración(text, src=src, targ=targ,
                        user=user, max_sols=max_sols, translate=translate,
                        connect=connect, generate=generate, html=html, choose=choose,
                        verbosity=verbosity)

## Cargar castellano y guaraní. Devuelve las 2 lenguas.
def cargar(reverse=False, bidir=False):
    src, targ = ('grn', 'spa') if reverse else ('spa', 'grn')
    source, target = mbojereha.Language.load_trans(src, targ, bidir=bidir)
    return source, target

