# ./_com.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:1c06abdc99453cc1e399eecb45b4dd01ec9af52b
# Generated 2019-06-06 19:25:21.342029 by PyXB version 1.2.6 using Python 3.6.7.final.0
# Namespace SRA.common [xmlns:com]

from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import pyxb.utils.six as _six
# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:0ed5619e-8880-11e9-9350-b0c090509cda')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.6'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# A holder for module-level binding classes so we can access them from
# inside class definitions where property names may conflict.
_module_typeBindings = pyxb.utils.utility.Object()

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('SRA.common', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement, default_namespace=default_namespace)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Atomic simple type: [anonymous]
class STD_ANON (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 379, 40)
    _Documentation = None
STD_ANON._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON, enum_prefix=None)
STD_ANON.Application_Read = STD_ANON._CF_enumeration.addEnumeration(unicode_value='Application Read', tag='Application_Read')
STD_ANON.Technical_Read = STD_ANON._CF_enumeration.addEnumeration(unicode_value='Technical Read', tag='Technical_Read')
STD_ANON._InitializeFacetMap(STD_ANON._CF_enumeration)
_module_typeBindings.STD_ANON = STD_ANON

# Atomic simple type: [anonymous]
class STD_ANON_ (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 387, 40)
    _Documentation = None
STD_ANON_._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_, enum_prefix=None)
STD_ANON_.Forward = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='Forward', tag='Forward')
STD_ANON_.Reverse = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='Reverse', tag='Reverse')
STD_ANON_.Adapter = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='Adapter', tag='Adapter')
STD_ANON_.Primer = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='Primer', tag='Primer')
STD_ANON_.Linker = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='Linker', tag='Linker')
STD_ANON_.BarCode = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='BarCode', tag='BarCode')
STD_ANON_.Other = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
STD_ANON_._InitializeFacetMap(STD_ANON_._CF_enumeration)
_module_typeBindings.STD_ANON_ = STD_ANON_

# Atomic simple type: [anonymous]
class STD_ANON_2 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 487, 50)
    _Documentation = None
STD_ANON_2._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_2, enum_prefix=None)
STD_ANON_2.full = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='full', tag='full')
STD_ANON_2.start = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='start', tag='start')
STD_ANON_2.end = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='end', tag='end')
STD_ANON_2._InitializeFacetMap(STD_ANON_2._CF_enumeration)
_module_typeBindings.STD_ANON_2 = STD_ANON_2

# Atomic simple type: [anonymous]
class STD_ANON_3 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 680, 16)
    _Documentation = None
STD_ANON_3._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_3, enum_prefix=None)
STD_ANON_3.leave_as_pool = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='leave_as_pool', tag='leave_as_pool')
STD_ANON_3.submitter_demultiplexed = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='submitter_demultiplexed', tag='submitter_demultiplexed')
STD_ANON_3._InitializeFacetMap(STD_ANON_3._CF_enumeration)
_module_typeBindings.STD_ANON_3 = STD_ANON_3

# Atomic simple type: {SRA.common}type454Model
class type454Model (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'type454Model')
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 894, 4)
    _Documentation = None
type454Model._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=type454Model, enum_prefix=None)
type454Model.n454_GS = type454Model._CF_enumeration.addEnumeration(unicode_value='454 GS', tag='n454_GS')
type454Model.n454_GS_20 = type454Model._CF_enumeration.addEnumeration(unicode_value='454 GS 20', tag='n454_GS_20')
type454Model.n454_GS_FLX = type454Model._CF_enumeration.addEnumeration(unicode_value='454 GS FLX', tag='n454_GS_FLX')
type454Model.n454_GS_FLX_ = type454Model._CF_enumeration.addEnumeration(unicode_value='454 GS FLX+', tag='n454_GS_FLX_')
type454Model.n454_GS_FLX_Titanium = type454Model._CF_enumeration.addEnumeration(unicode_value='454 GS FLX Titanium', tag='n454_GS_FLX_Titanium')
type454Model.n454_GS_Junior = type454Model._CF_enumeration.addEnumeration(unicode_value='454 GS Junior', tag='n454_GS_Junior')
type454Model.unspecified = type454Model._CF_enumeration.addEnumeration(unicode_value='unspecified', tag='unspecified')
type454Model._InitializeFacetMap(type454Model._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'type454Model', type454Model)
_module_typeBindings.type454Model = type454Model

# Atomic simple type: {SRA.common}typeIlluminaModel
class typeIlluminaModel (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'typeIlluminaModel')
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 906, 4)
    _Documentation = None
typeIlluminaModel._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=typeIlluminaModel, enum_prefix=None)
typeIlluminaModel.HiSeq_X_Five = typeIlluminaModel._CF_enumeration.addEnumeration(unicode_value='HiSeq X Five', tag='HiSeq_X_Five')
typeIlluminaModel.HiSeq_X_Ten = typeIlluminaModel._CF_enumeration.addEnumeration(unicode_value='HiSeq X Ten', tag='HiSeq_X_Ten')
typeIlluminaModel.Illumina_Genome_Analyzer = typeIlluminaModel._CF_enumeration.addEnumeration(unicode_value='Illumina Genome Analyzer', tag='Illumina_Genome_Analyzer')
typeIlluminaModel.Illumina_Genome_Analyzer_II = typeIlluminaModel._CF_enumeration.addEnumeration(unicode_value='Illumina Genome Analyzer II', tag='Illumina_Genome_Analyzer_II')
typeIlluminaModel.Illumina_Genome_Analyzer_IIx = typeIlluminaModel._CF_enumeration.addEnumeration(unicode_value='Illumina Genome Analyzer IIx', tag='Illumina_Genome_Analyzer_IIx')
typeIlluminaModel.Illumina_HiScanSQ = typeIlluminaModel._CF_enumeration.addEnumeration(unicode_value='Illumina HiScanSQ', tag='Illumina_HiScanSQ')
typeIlluminaModel.Illumina_HiSeq_1000 = typeIlluminaModel._CF_enumeration.addEnumeration(unicode_value='Illumina HiSeq 1000', tag='Illumina_HiSeq_1000')
typeIlluminaModel.Illumina_HiSeq_1500 = typeIlluminaModel._CF_enumeration.addEnumeration(unicode_value='Illumina HiSeq 1500', tag='Illumina_HiSeq_1500')
typeIlluminaModel.Illumina_HiSeq_2000 = typeIlluminaModel._CF_enumeration.addEnumeration(unicode_value='Illumina HiSeq 2000', tag='Illumina_HiSeq_2000')
typeIlluminaModel.Illumina_HiSeq_2500 = typeIlluminaModel._CF_enumeration.addEnumeration(unicode_value='Illumina HiSeq 2500', tag='Illumina_HiSeq_2500')
typeIlluminaModel.Illumina_HiSeq_3000 = typeIlluminaModel._CF_enumeration.addEnumeration(unicode_value='Illumina HiSeq 3000', tag='Illumina_HiSeq_3000')
typeIlluminaModel.Illumina_HiSeq_4000 = typeIlluminaModel._CF_enumeration.addEnumeration(unicode_value='Illumina HiSeq 4000', tag='Illumina_HiSeq_4000')
typeIlluminaModel.Illumina_MiSeq = typeIlluminaModel._CF_enumeration.addEnumeration(unicode_value='Illumina MiSeq', tag='Illumina_MiSeq')
typeIlluminaModel.Illumina_MiniSeq = typeIlluminaModel._CF_enumeration.addEnumeration(unicode_value='Illumina MiniSeq', tag='Illumina_MiniSeq')
typeIlluminaModel.Illumina_NovaSeq_6000 = typeIlluminaModel._CF_enumeration.addEnumeration(unicode_value='Illumina NovaSeq 6000', tag='Illumina_NovaSeq_6000')
typeIlluminaModel.NextSeq_500 = typeIlluminaModel._CF_enumeration.addEnumeration(unicode_value='NextSeq 500', tag='NextSeq_500')
typeIlluminaModel.NextSeq_550 = typeIlluminaModel._CF_enumeration.addEnumeration(unicode_value='NextSeq 550', tag='NextSeq_550')
typeIlluminaModel.unspecified = typeIlluminaModel._CF_enumeration.addEnumeration(unicode_value='unspecified', tag='unspecified')
typeIlluminaModel._InitializeFacetMap(typeIlluminaModel._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'typeIlluminaModel', typeIlluminaModel)
_module_typeBindings.typeIlluminaModel = typeIlluminaModel

# Atomic simple type: {SRA.common}typeHelicosModel
class typeHelicosModel (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'typeHelicosModel')
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 929, 4)
    _Documentation = None
typeHelicosModel._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=typeHelicosModel, enum_prefix=None)
typeHelicosModel.Helicos_HeliScope = typeHelicosModel._CF_enumeration.addEnumeration(unicode_value='Helicos HeliScope', tag='Helicos_HeliScope')
typeHelicosModel.unspecified = typeHelicosModel._CF_enumeration.addEnumeration(unicode_value='unspecified', tag='unspecified')
typeHelicosModel._InitializeFacetMap(typeHelicosModel._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'typeHelicosModel', typeHelicosModel)
_module_typeBindings.typeHelicosModel = typeHelicosModel

# Atomic simple type: {SRA.common}typeAbiSolidModel
class typeAbiSolidModel (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'typeAbiSolidModel')
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 936, 4)
    _Documentation = None
typeAbiSolidModel._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=typeAbiSolidModel, enum_prefix=None)
typeAbiSolidModel.AB_SOLiD_System = typeAbiSolidModel._CF_enumeration.addEnumeration(unicode_value='AB SOLiD System', tag='AB_SOLiD_System')
typeAbiSolidModel.AB_SOLiD_System_2_0 = typeAbiSolidModel._CF_enumeration.addEnumeration(unicode_value='AB SOLiD System 2.0', tag='AB_SOLiD_System_2_0')
typeAbiSolidModel.AB_SOLiD_System_3_0 = typeAbiSolidModel._CF_enumeration.addEnumeration(unicode_value='AB SOLiD System 3.0', tag='AB_SOLiD_System_3_0')
typeAbiSolidModel.AB_SOLiD_3_Plus_System = typeAbiSolidModel._CF_enumeration.addEnumeration(unicode_value='AB SOLiD 3 Plus System', tag='AB_SOLiD_3_Plus_System')
typeAbiSolidModel.AB_SOLiD_4_System = typeAbiSolidModel._CF_enumeration.addEnumeration(unicode_value='AB SOLiD 4 System', tag='AB_SOLiD_4_System')
typeAbiSolidModel.AB_SOLiD_4hq_System = typeAbiSolidModel._CF_enumeration.addEnumeration(unicode_value='AB SOLiD 4hq System', tag='AB_SOLiD_4hq_System')
typeAbiSolidModel.AB_SOLiD_PI_System = typeAbiSolidModel._CF_enumeration.addEnumeration(unicode_value='AB SOLiD PI System', tag='AB_SOLiD_PI_System')
typeAbiSolidModel.AB_5500_Genetic_Analyzer = typeAbiSolidModel._CF_enumeration.addEnumeration(unicode_value='AB 5500 Genetic Analyzer', tag='AB_5500_Genetic_Analyzer')
typeAbiSolidModel.AB_5500xl_Genetic_Analyzer = typeAbiSolidModel._CF_enumeration.addEnumeration(unicode_value='AB 5500xl Genetic Analyzer', tag='AB_5500xl_Genetic_Analyzer')
typeAbiSolidModel.AB_5500xl_W_Genetic_Analysis_System = typeAbiSolidModel._CF_enumeration.addEnumeration(unicode_value='AB 5500xl-W Genetic Analysis System', tag='AB_5500xl_W_Genetic_Analysis_System')
typeAbiSolidModel.unspecified = typeAbiSolidModel._CF_enumeration.addEnumeration(unicode_value='unspecified', tag='unspecified')
typeAbiSolidModel._InitializeFacetMap(typeAbiSolidModel._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'typeAbiSolidModel', typeAbiSolidModel)
_module_typeBindings.typeAbiSolidModel = typeAbiSolidModel

# Atomic simple type: {SRA.common}typeCGModel
class typeCGModel (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'typeCGModel')
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 956, 4)
    _Documentation = None
typeCGModel._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=typeCGModel, enum_prefix=None)
typeCGModel.Complete_Genomics = typeCGModel._CF_enumeration.addEnumeration(unicode_value='Complete Genomics', tag='Complete_Genomics')
typeCGModel.unspecified = typeCGModel._CF_enumeration.addEnumeration(unicode_value='unspecified', tag='unspecified')
typeCGModel._InitializeFacetMap(typeCGModel._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'typeCGModel', typeCGModel)
_module_typeBindings.typeCGModel = typeCGModel

# Atomic simple type: {SRA.common}typeBGISEQModel
class typeBGISEQModel (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'typeBGISEQModel')
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 963, 4)
    _Documentation = None
typeBGISEQModel._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=typeBGISEQModel, enum_prefix=None)
typeBGISEQModel.BGISEQ_500 = typeBGISEQModel._CF_enumeration.addEnumeration(unicode_value='BGISEQ-500', tag='BGISEQ_500')
typeBGISEQModel._InitializeFacetMap(typeBGISEQModel._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'typeBGISEQModel', typeBGISEQModel)
_module_typeBindings.typeBGISEQModel = typeBGISEQModel

# Atomic simple type: {SRA.common}typePacBioModel
class typePacBioModel (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'typePacBioModel')
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 969, 4)
    _Documentation = None
typePacBioModel._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=typePacBioModel, enum_prefix=None)
typePacBioModel.PacBio_RS = typePacBioModel._CF_enumeration.addEnumeration(unicode_value='PacBio RS', tag='PacBio_RS')
typePacBioModel.PacBio_RS_II = typePacBioModel._CF_enumeration.addEnumeration(unicode_value='PacBio RS II', tag='PacBio_RS_II')
typePacBioModel.Sequel = typePacBioModel._CF_enumeration.addEnumeration(unicode_value='Sequel', tag='Sequel')
typePacBioModel.unspecified = typePacBioModel._CF_enumeration.addEnumeration(unicode_value='unspecified', tag='unspecified')
typePacBioModel._InitializeFacetMap(typePacBioModel._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'typePacBioModel', typePacBioModel)
_module_typeBindings.typePacBioModel = typePacBioModel

# Atomic simple type: {SRA.common}typeIontorrentModel
class typeIontorrentModel (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'typeIontorrentModel')
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 978, 4)
    _Documentation = None
typeIontorrentModel._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=typeIontorrentModel, enum_prefix=None)
typeIontorrentModel.Ion_Torrent_PGM = typeIontorrentModel._CF_enumeration.addEnumeration(unicode_value='Ion Torrent PGM', tag='Ion_Torrent_PGM')
typeIontorrentModel.Ion_Torrent_Proton = typeIontorrentModel._CF_enumeration.addEnumeration(unicode_value='Ion Torrent Proton', tag='Ion_Torrent_Proton')
typeIontorrentModel.Ion_Torrent_S5 = typeIontorrentModel._CF_enumeration.addEnumeration(unicode_value='Ion Torrent S5', tag='Ion_Torrent_S5')
typeIontorrentModel.Ion_Torrent_S5_XL = typeIontorrentModel._CF_enumeration.addEnumeration(unicode_value='Ion Torrent S5 XL', tag='Ion_Torrent_S5_XL')
typeIontorrentModel.unspecified = typeIontorrentModel._CF_enumeration.addEnumeration(unicode_value='unspecified', tag='unspecified')
typeIontorrentModel._InitializeFacetMap(typeIontorrentModel._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'typeIontorrentModel', typeIontorrentModel)
_module_typeBindings.typeIontorrentModel = typeIontorrentModel

# Atomic simple type: {SRA.common}typeCapillaryModel
class typeCapillaryModel (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'typeCapillaryModel')
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 988, 4)
    _Documentation = None
typeCapillaryModel._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=typeCapillaryModel, enum_prefix=None)
typeCapillaryModel.AB_3730xL_Genetic_Analyzer = typeCapillaryModel._CF_enumeration.addEnumeration(unicode_value='AB 3730xL Genetic Analyzer', tag='AB_3730xL_Genetic_Analyzer')
typeCapillaryModel.AB_3730_Genetic_Analyzer = typeCapillaryModel._CF_enumeration.addEnumeration(unicode_value='AB 3730 Genetic Analyzer', tag='AB_3730_Genetic_Analyzer')
typeCapillaryModel.AB_3500xL_Genetic_Analyzer = typeCapillaryModel._CF_enumeration.addEnumeration(unicode_value='AB 3500xL Genetic Analyzer', tag='AB_3500xL_Genetic_Analyzer')
typeCapillaryModel.AB_3500_Genetic_Analyzer = typeCapillaryModel._CF_enumeration.addEnumeration(unicode_value='AB 3500 Genetic Analyzer', tag='AB_3500_Genetic_Analyzer')
typeCapillaryModel.AB_3130xL_Genetic_Analyzer = typeCapillaryModel._CF_enumeration.addEnumeration(unicode_value='AB 3130xL Genetic Analyzer', tag='AB_3130xL_Genetic_Analyzer')
typeCapillaryModel.AB_3130_Genetic_Analyzer = typeCapillaryModel._CF_enumeration.addEnumeration(unicode_value='AB 3130 Genetic Analyzer', tag='AB_3130_Genetic_Analyzer')
typeCapillaryModel.AB_310_Genetic_Analyzer = typeCapillaryModel._CF_enumeration.addEnumeration(unicode_value='AB 310 Genetic Analyzer', tag='AB_310_Genetic_Analyzer')
typeCapillaryModel.unspecified = typeCapillaryModel._CF_enumeration.addEnumeration(unicode_value='unspecified', tag='unspecified')
typeCapillaryModel._InitializeFacetMap(typeCapillaryModel._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'typeCapillaryModel', typeCapillaryModel)
_module_typeBindings.typeCapillaryModel = typeCapillaryModel

# Atomic simple type: {SRA.common}typeOxfordNanoporeModel
class typeOxfordNanoporeModel (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'typeOxfordNanoporeModel')
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 1001, 4)
    _Documentation = None
typeOxfordNanoporeModel._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=typeOxfordNanoporeModel, enum_prefix=None)
typeOxfordNanoporeModel.MinION = typeOxfordNanoporeModel._CF_enumeration.addEnumeration(unicode_value='MinION', tag='MinION')
typeOxfordNanoporeModel.GridION = typeOxfordNanoporeModel._CF_enumeration.addEnumeration(unicode_value='GridION', tag='GridION')
typeOxfordNanoporeModel.PromethION = typeOxfordNanoporeModel._CF_enumeration.addEnumeration(unicode_value='PromethION', tag='PromethION')
typeOxfordNanoporeModel.unspecified = typeOxfordNanoporeModel._CF_enumeration.addEnumeration(unicode_value='unspecified', tag='unspecified')
typeOxfordNanoporeModel._InitializeFacetMap(typeOxfordNanoporeModel._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'typeOxfordNanoporeModel', typeOxfordNanoporeModel)
_module_typeBindings.typeOxfordNanoporeModel = typeOxfordNanoporeModel

# Complex type {SRA.common}ObjectType with content type ELEMENT_ONLY
class ObjectType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {SRA.common}ObjectType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ObjectType')
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 17, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element IDENTIFIERS uses Python identifier IDENTIFIERS
    __IDENTIFIERS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'IDENTIFIERS'), 'IDENTIFIERS', '__SRA_common_ObjectType_IDENTIFIERS', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 19, 12), )

    
    IDENTIFIERS = property(__IDENTIFIERS.value, __IDENTIFIERS.set, None, None)

    
    # Attribute alias uses Python identifier alias
    __alias = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'alias'), 'alias', '__SRA_common_ObjectType_alias', pyxb.binding.datatypes.string)
    __alias._DeclarationLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 21, 8)
    __alias._UseLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 21, 8)
    
    alias = property(__alias.value, __alias.set, None, '\n                    Submitter designated name for the object. The name must be unique within the submission account.\n                ')

    
    # Attribute center_name uses Python identifier center_name
    __center_name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'center_name'), 'center_name', '__SRA_common_ObjectType_center_name', pyxb.binding.datatypes.string)
    __center_name._DeclarationLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 28, 8)
    __center_name._UseLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 28, 8)
    
    center_name = property(__center_name.value, __center_name.set, None, '\n                    The center name of the submitter.\n                ')

    
    # Attribute broker_name uses Python identifier broker_name
    __broker_name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'broker_name'), 'broker_name', '__SRA_common_ObjectType_broker_name', pyxb.binding.datatypes.string)
    __broker_name._DeclarationLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 35, 8)
    __broker_name._UseLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 35, 8)
    
    broker_name = property(__broker_name.value, __broker_name.set, None, '\n                    The center name of the broker.\n                ')

    
    # Attribute accession uses Python identifier accession
    __accession = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'accession'), 'accession', '__SRA_common_ObjectType_accession', pyxb.binding.datatypes.string)
    __accession._DeclarationLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 42, 8)
    __accession._UseLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 42, 8)
    
    accession = property(__accession.value, __accession.set, None, '\n                    The object accession assigned by the archive.\n                ')

    _ElementMap.update({
        __IDENTIFIERS.name() : __IDENTIFIERS
    })
    _AttributeMap.update({
        __alias.name() : __alias,
        __center_name.name() : __center_name,
        __broker_name.name() : __broker_name,
        __accession.name() : __accession
    })
_module_typeBindings.ObjectType = ObjectType
Namespace.addCategoryObject('typeBinding', 'ObjectType', ObjectType)


# Complex type {SRA.common}RefObjectType with content type ELEMENT_ONLY
class RefObjectType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {SRA.common}RefObjectType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RefObjectType')
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 51, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element IDENTIFIERS uses Python identifier IDENTIFIERS
    __IDENTIFIERS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'IDENTIFIERS'), 'IDENTIFIERS', '__SRA_common_RefObjectType_IDENTIFIERS', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 53, 12), )

    
    IDENTIFIERS = property(__IDENTIFIERS.value, __IDENTIFIERS.set, None, None)

    
    # Attribute refname uses Python identifier refname
    __refname = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'refname'), 'refname', '__SRA_common_RefObjectType_refname', pyxb.binding.datatypes.string)
    __refname._DeclarationLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 55, 8)
    __refname._UseLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 55, 8)
    
    refname = property(__refname.value, __refname.set, None, '\n                    Identifies an object by name within the namespace defined by attribute "refcenter".\n                ')

    
    # Attribute refcenter uses Python identifier refcenter
    __refcenter = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'refcenter'), 'refcenter', '__SRA_common_RefObjectType_refcenter', pyxb.binding.datatypes.string)
    __refcenter._DeclarationLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 62, 8)
    __refcenter._UseLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 62, 8)
    
    refcenter = property(__refcenter.value, __refcenter.set, None, '\n                    The namespace of the attribute "refname".\n                ')

    
    # Attribute accession uses Python identifier accession
    __accession = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'accession'), 'accession', '__SRA_common_RefObjectType_accession', pyxb.binding.datatypes.string)
    __accession._DeclarationLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 69, 8)
    __accession._UseLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 69, 8)
    
    accession = property(__accession.value, __accession.set, None, '\n                    Identifies a record by its accession.  The scope of resolution is the entire Archive.\n                ')

    _ElementMap.update({
        __IDENTIFIERS.name() : __IDENTIFIERS
    })
    _AttributeMap.update({
        __refname.name() : __refname,
        __refcenter.name() : __refcenter,
        __accession.name() : __accession
    })
_module_typeBindings.RefObjectType = RefObjectType
Namespace.addCategoryObject('typeBinding', 'RefObjectType', RefObjectType)


# Complex type {SRA.common}NameType with content type SIMPLE
class NameType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {SRA.common}NameType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'NameType')
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 138, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute label uses Python identifier label
    __label = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'label'), 'label', '__SRA_common_NameType_label', pyxb.binding.datatypes.string)
    __label._DeclarationLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 141, 16)
    __label._UseLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 141, 16)
    
    label = property(__label.value, __label.set, None, 'Alternative/explanatory description of the same object/identifier.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __label.name() : __label
    })
_module_typeBindings.NameType = NameType
Namespace.addCategoryObject('typeBinding', 'NameType', NameType)


# Complex type {SRA.common}IdentifierType with content type ELEMENT_ONLY
class IdentifierType (pyxb.binding.basis.complexTypeDefinition):
    """Set of record identifiers."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'IdentifierType')
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 163, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element PRIMARY_ID uses Python identifier PRIMARY_ID
    __PRIMARY_ID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'PRIMARY_ID'), 'PRIMARY_ID', '__SRA_common_IdentifierType_PRIMARY_ID', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 168, 12), )

    
    PRIMARY_ID = property(__PRIMARY_ID.value, __PRIMARY_ID.set, None, 'A primary identifier in the INSDC namespace.')

    
    # Element SECONDARY_ID uses Python identifier SECONDARY_ID
    __SECONDARY_ID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'SECONDARY_ID'), 'SECONDARY_ID', '__SRA_common_IdentifierType_SECONDARY_ID', True, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 173, 12), )

    
    SECONDARY_ID = property(__SECONDARY_ID.value, __SECONDARY_ID.set, None, 'A secondary identifier in the INSDC namespace.')

    
    # Element EXTERNAL_ID uses Python identifier EXTERNAL_ID
    __EXTERNAL_ID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'EXTERNAL_ID'), 'EXTERNAL_ID', '__SRA_common_IdentifierType_EXTERNAL_ID', True, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 178, 12), )

    
    EXTERNAL_ID = property(__EXTERNAL_ID.value, __EXTERNAL_ID.set, None, 'An identifer rom a public non-INSDC resource.')

    
    # Element SUBMITTER_ID uses Python identifier SUBMITTER_ID
    __SUBMITTER_ID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'SUBMITTER_ID'), 'SUBMITTER_ID', '__SRA_common_IdentifierType_SUBMITTER_ID', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 184, 12), )

    
    SUBMITTER_ID = property(__SUBMITTER_ID.value, __SUBMITTER_ID.set, None, 'A submitter provided identifier.')

    
    # Element UUID uses Python identifier UUID
    __UUID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'UUID'), 'UUID', '__SRA_common_IdentifierType_UUID', True, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 189, 12), )

    
    UUID = property(__UUID.value, __UUID.set, None, 'A universally unique identifier that requires no namespace.')

    _ElementMap.update({
        __PRIMARY_ID.name() : __PRIMARY_ID,
        __SECONDARY_ID.name() : __SECONDARY_ID,
        __EXTERNAL_ID.name() : __EXTERNAL_ID,
        __SUBMITTER_ID.name() : __SUBMITTER_ID,
        __UUID.name() : __UUID
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.IdentifierType = IdentifierType
Namespace.addCategoryObject('typeBinding', 'IdentifierType', IdentifierType)


# Complex type {SRA.common}XRefType with content type ELEMENT_ONLY
class XRefType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {SRA.common}XRefType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'XRefType')
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 196, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element DB uses Python identifier DB
    __DB = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'DB'), 'DB', '__SRA_common_XRefType_DB', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 198, 12), )

    
    DB = property(__DB.value, __DB.set, None, ' INSDC controlled vocabulary of permitted cross references.\n                        Please see http://www.insdc.org/db_xref.html . For example, FLYBASE. ')

    
    # Element ID uses Python identifier ID
    __ID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ID'), 'ID', '__SRA_common_XRefType_ID', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 204, 12), )

    
    ID = property(__ID.value, __ID.set, None, '\n                            Accession in the referenced database.    For example,  FBtr0080008 (in FLYBASE).\n                        ')

    
    # Element LABEL uses Python identifier LABEL
    __LABEL = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'LABEL'), 'LABEL', '__SRA_common_XRefType_LABEL', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 211, 12), )

    
    LABEL = property(__LABEL.value, __LABEL.set, None, '\n                            Text label to display for the link.\n                        ')

    _ElementMap.update({
        __DB.name() : __DB,
        __ID.name() : __ID,
        __LABEL.name() : __LABEL
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.XRefType = XRefType
Namespace.addCategoryObject('typeBinding', 'XRefType', XRefType)


# Complex type {SRA.common}URLType with content type ELEMENT_ONLY
class URLType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {SRA.common}URLType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'URLType')
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 221, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element LABEL uses Python identifier LABEL
    __LABEL = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'LABEL'), 'LABEL', '__SRA_common_URLType_LABEL', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 223, 12), )

    
    LABEL = property(__LABEL.value, __LABEL.set, None, '\n                        Text label to display for the link.\n                    ')

    
    # Element URL uses Python identifier URL
    __URL = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'URL'), 'URL', '__SRA_common_URLType_URL', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 230, 12), )

    
    URL = property(__URL.value, __URL.set, None, '\n                        The internet service link (file:, http:, ftp:, etc).\n                    ')

    _ElementMap.update({
        __LABEL.name() : __LABEL,
        __URL.name() : __URL
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.URLType = URLType
Namespace.addCategoryObject('typeBinding', 'URLType', URLType)


# Complex type {SRA.common}AttributeType with content type ELEMENT_ONLY
class AttributeType (pyxb.binding.basis.complexTypeDefinition):
    """
                Reusable attributes to encode tag-value pairs with optional units.
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AttributeType')
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 239, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element TAG uses Python identifier TAG
    __TAG = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'TAG'), 'TAG', '__SRA_common_AttributeType_TAG', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 246, 12), )

    
    TAG = property(__TAG.value, __TAG.set, None, '\n                        Name of the attribute.\n                    ')

    
    # Element VALUE uses Python identifier VALUE
    __VALUE = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'VALUE'), 'VALUE', '__SRA_common_AttributeType_VALUE', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 253, 12), )

    
    VALUE = property(__VALUE.value, __VALUE.set, None, '\n                        Value of the attribute.\n                    ')

    
    # Element UNITS uses Python identifier UNITS
    __UNITS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'UNITS'), 'UNITS', '__SRA_common_AttributeType_UNITS', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 260, 12), )

    
    UNITS = property(__UNITS.value, __UNITS.set, None, '\n                        Optional scientific units.\n                    ')

    _ElementMap.update({
        __TAG.name() : __TAG,
        __VALUE.name() : __VALUE,
        __UNITS.name() : __UNITS
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AttributeType = AttributeType
Namespace.addCategoryObject('typeBinding', 'AttributeType', AttributeType)


# Complex type {SRA.common}LinkType with content type ELEMENT_ONLY
class LinkType (pyxb.binding.basis.complexTypeDefinition):
    """
                Reusable external links type to encode URL links, Entrez links, and db_xref links.
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LinkType')
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 270, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element URL_LINK uses Python identifier URL_LINK
    __URL_LINK = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'URL_LINK'), 'URL_LINK', '__SRA_common_LinkType_URL_LINK', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 277, 12), )

    
    URL_LINK = property(__URL_LINK.value, __URL_LINK.set, None, None)

    
    # Element XREF_LINK uses Python identifier XREF_LINK
    __XREF_LINK = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'XREF_LINK'), 'XREF_LINK', '__SRA_common_LinkType_XREF_LINK', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 295, 12), )

    
    XREF_LINK = property(__XREF_LINK.value, __XREF_LINK.set, None, None)

    
    # Element ENTREZ_LINK uses Python identifier ENTREZ_LINK
    __ENTREZ_LINK = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ENTREZ_LINK'), 'ENTREZ_LINK', '__SRA_common_LinkType_ENTREZ_LINK', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 297, 12), )

    
    ENTREZ_LINK = property(__ENTREZ_LINK.value, __ENTREZ_LINK.set, None, None)

    _ElementMap.update({
        __URL_LINK.name() : __URL_LINK,
        __XREF_LINK.name() : __XREF_LINK,
        __ENTREZ_LINK.name() : __ENTREZ_LINK
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.LinkType = LinkType
Namespace.addCategoryObject('typeBinding', 'LinkType', LinkType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 278, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element LABEL uses Python identifier LABEL
    __LABEL = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'LABEL'), 'LABEL', '__SRA_common_CTD_ANON_LABEL', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 280, 24), )

    
    LABEL = property(__LABEL.value, __LABEL.set, None, '\n                                    Text label to display for the link.\n                                ')

    
    # Element URL uses Python identifier URL
    __URL = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'URL'), 'URL', '__SRA_common_CTD_ANON_URL', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 287, 24), )

    
    URL = property(__URL.value, __URL.set, None, ' The internet service link (file:, http:, ftp: etc). ')

    _ElementMap.update({
        __LABEL.name() : __LABEL,
        __URL.name() : __URL
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON = CTD_ANON


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 298, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element DB uses Python identifier DB
    __DB = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'DB'), 'DB', '__SRA_common_CTD_ANON__DB', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 300, 24), )

    
    DB = property(__DB.value, __DB.set, None, '\n                                    NCBI controlled vocabulary of permitted cross references.  Please see http://www.ncbi.nlm.nih.gov/entrez/eutils/einfo.fcgi? .\n                                ')

    
    # Element ID uses Python identifier ID
    __ID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ID'), 'ID', '__SRA_common_CTD_ANON__ID', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 308, 28), )

    
    ID = property(__ID.value, __ID.set, None, '\n                                        Numeric record id meaningful to the NCBI Entrez system.\n                                    ')

    
    # Element QUERY uses Python identifier QUERY
    __QUERY = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'QUERY'), 'QUERY', '__SRA_common_CTD_ANON__QUERY', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 316, 28), )

    
    QUERY = property(__QUERY.value, __QUERY.set, None, '\n                                        Accession string meaningful to the NCBI Entrez system.\n                                    ')

    
    # Element LABEL uses Python identifier LABEL
    __LABEL = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'LABEL'), 'LABEL', '__SRA_common_CTD_ANON__LABEL', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 324, 24), )

    
    LABEL = property(__LABEL.value, __LABEL.set, None, '\n                                    How to label the link.\n                                ')

    _ElementMap.update({
        __DB.name() : __DB,
        __ID.name() : __ID,
        __QUERY.name() : __QUERY,
        __LABEL.name() : __LABEL
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_ = CTD_ANON_


# Complex type {SRA.common}SpotDescriptorType with content type ELEMENT_ONLY
class SpotDescriptorType (pyxb.binding.basis.complexTypeDefinition):
    """
                    The SPOT_DESCRIPTOR specifies how to decode the individual reads of interest from the 
                    monolithic spot sequence.  The spot descriptor contains aspects of the experimental design, 
                    platform, and processing information.  There will be two methods of specification: one 
                    will be an index into a table of typical decodings, the other being an exact specification.                                      
                """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SpotDescriptorType')
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 339, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element SPOT_DECODE_SPEC uses Python identifier SPOT_DECODE_SPEC
    __SPOT_DECODE_SPEC = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'SPOT_DECODE_SPEC'), 'SPOT_DECODE_SPEC', '__SRA_common_SpotDescriptorType_SPOT_DECODE_SPEC', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 349, 12), )

    
    SPOT_DECODE_SPEC = property(__SPOT_DECODE_SPEC.value, __SPOT_DECODE_SPEC.set, None, None)

    _ElementMap.update({
        __SPOT_DECODE_SPEC.name() : __SPOT_DECODE_SPEC
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.SpotDescriptorType = SpotDescriptorType
Namespace.addCategoryObject('typeBinding', 'SpotDescriptorType', SpotDescriptorType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 350, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element SPOT_LENGTH uses Python identifier SPOT_LENGTH
    __SPOT_LENGTH = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'SPOT_LENGTH'), 'SPOT_LENGTH', '__SRA_common_CTD_ANON_2_SPOT_LENGTH', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 352, 24), )

    
    SPOT_LENGTH = property(__SPOT_LENGTH.value, __SPOT_LENGTH.set, None, ' Number of base/color calls, cycles, or flows per\n                                    spot (raw sequence length or flow length including all\n                                    application and technical tags and mate pairs, but not including\n                                    gap lengths). This value will be platform dependent, library\n                                    dependent, and possibly run dependent. Variable length platforms\n                                    will still have a constant flow/cycle length. ')

    
    # Element READ_SPEC uses Python identifier READ_SPEC
    __READ_SPEC = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'READ_SPEC'), 'READ_SPEC', '__SRA_common_CTD_ANON_2_READ_SPEC', True, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 363, 24), )

    
    READ_SPEC = property(__READ_SPEC.value, __READ_SPEC.set, None, None)

    _ElementMap.update({
        __SPOT_LENGTH.name() : __SPOT_LENGTH,
        __READ_SPEC.name() : __READ_SPEC
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_2 = CTD_ANON_2


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 364, 28)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element READ_INDEX uses Python identifier READ_INDEX
    __READ_INDEX = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'READ_INDEX'), 'READ_INDEX', '__SRA_common_CTD_ANON_3_READ_INDEX', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 366, 36), )

    
    READ_INDEX = property(__READ_INDEX.value, __READ_INDEX.set, None, 'READ_INDEX starts at 0 and is incrementally increased for each sequential READ_SPEC within a SPOT_DECODE_SPEC')

    
    # Element READ_LABEL uses Python identifier READ_LABEL
    __READ_LABEL = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'READ_LABEL'), 'READ_LABEL', '__SRA_common_CTD_ANON_3_READ_LABEL', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 372, 36), )

    
    READ_LABEL = property(__READ_LABEL.value, __READ_LABEL.set, None, 'READ_LABEL is a name for this tag, and can be used to on output to determine read name, for example F or R.')

    
    # Element READ_CLASS uses Python identifier READ_CLASS
    __READ_CLASS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'READ_CLASS'), 'READ_CLASS', '__SRA_common_CTD_ANON_3_READ_CLASS', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 378, 36), )

    
    READ_CLASS = property(__READ_CLASS.value, __READ_CLASS.set, None, None)

    
    # Element READ_TYPE uses Python identifier READ_TYPE
    __READ_TYPE = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'READ_TYPE'), 'READ_TYPE', '__SRA_common_CTD_ANON_3_READ_TYPE', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 386, 36), )

    
    READ_TYPE = property(__READ_TYPE.value, __READ_TYPE.set, None, None)

    
    # Element RELATIVE_ORDER uses Python identifier RELATIVE_ORDER
    __RELATIVE_ORDER = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'RELATIVE_ORDER'), 'RELATIVE_ORDER', '__SRA_common_CTD_ANON_3_RELATIVE_ORDER', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 406, 40), )

    
    RELATIVE_ORDER = property(__RELATIVE_ORDER.value, __RELATIVE_ORDER.set, None, '\n                                                        The read is located beginning at the offset or cycle relative to another read.  \n                                                        This choice is appropriate for example when specifying a read\n                                                        that follows a variable length expected sequence(s).\n                                                    ')

    
    # Element BASE_COORD uses Python identifier BASE_COORD
    __BASE_COORD = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'BASE_COORD'), 'BASE_COORD', '__SRA_common_CTD_ANON_3_BASE_COORD', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 433, 40), )

    
    BASE_COORD = property(__BASE_COORD.value, __BASE_COORD.set, None, '\n                                                        The location of the read start in terms of base count (1 is beginning of spot).\n                                                    ')

    
    # Element EXPECTED_BASECALL_TABLE uses Python identifier EXPECTED_BASECALL_TABLE
    __EXPECTED_BASECALL_TABLE = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'EXPECTED_BASECALL_TABLE'), 'EXPECTED_BASECALL_TABLE', '__SRA_common_CTD_ANON_3_EXPECTED_BASECALL_TABLE', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 440, 40), )

    
    EXPECTED_BASECALL_TABLE = property(__EXPECTED_BASECALL_TABLE.value, __EXPECTED_BASECALL_TABLE.set, None, '\n                                                        A set of choices of expected basecalls for a current read. Read will be zero-length if none is found.\n                                                    ')

    _ElementMap.update({
        __READ_INDEX.name() : __READ_INDEX,
        __READ_LABEL.name() : __READ_LABEL,
        __READ_CLASS.name() : __READ_CLASS,
        __READ_TYPE.name() : __READ_TYPE,
        __RELATIVE_ORDER.name() : __RELATIVE_ORDER,
        __BASE_COORD.name() : __BASE_COORD,
        __EXPECTED_BASECALL_TABLE.name() : __EXPECTED_BASECALL_TABLE
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_3 = CTD_ANON_3


# Complex type [anonymous] with content type EMPTY
class CTD_ANON_4 (pyxb.binding.basis.complexTypeDefinition):
    """
                                                        The read is located beginning at the offset or cycle relative to another read.  
                                                        This choice is appropriate for example when specifying a read
                                                        that follows a variable length expected sequence(s).
                                                    """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 414, 44)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute follows_read_index uses Python identifier follows_read_index
    __follows_read_index = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'follows_read_index'), 'follows_read_index', '__SRA_common_CTD_ANON_4_follows_read_index', pyxb.binding.datatypes.nonNegativeInteger)
    __follows_read_index._DeclarationLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 415, 48)
    __follows_read_index._UseLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 415, 48)
    
    follows_read_index = property(__follows_read_index.value, __follows_read_index.set, None, '\n                                                                Specify the read index that precedes this read.\n                                                            ')

    
    # Attribute precedes_read_index uses Python identifier precedes_read_index
    __precedes_read_index = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'precedes_read_index'), 'precedes_read_index', '__SRA_common_CTD_ANON_4_precedes_read_index', pyxb.binding.datatypes.nonNegativeInteger)
    __precedes_read_index._DeclarationLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 423, 48)
    __precedes_read_index._UseLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 423, 48)
    
    precedes_read_index = property(__precedes_read_index.value, __precedes_read_index.set, None, '\n                                                                Specify the read index that follows this read.\n                                                            ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __follows_read_index.name() : __follows_read_index,
        __precedes_read_index.name() : __precedes_read_index
    })
_module_typeBindings.CTD_ANON_4 = CTD_ANON_4


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_5 (pyxb.binding.basis.complexTypeDefinition):
    """
                                                        A set of choices of expected basecalls for a current read. Read will be zero-length if none is found.
                                                    """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 446, 44)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element BASECALL uses Python identifier BASECALL
    __BASECALL = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'BASECALL'), 'BASECALL', '__SRA_common_CTD_ANON_5_BASECALL', True, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 448, 50), )

    
    BASECALL = property(__BASECALL.value, __BASECALL.set, None, "\n                                                       Element's body contains a basecall, attribute provide description of this read meaning as well as matching rules.\n                                                  ")

    
    # Attribute default_length uses Python identifier default_length
    __default_length = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'default_length'), 'default_length', '__SRA_common_CTD_ANON_5_default_length', pyxb.binding.datatypes.nonNegativeInteger)
    __default_length._DeclarationLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 522, 48)
    __default_length._UseLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 522, 48)
    
    default_length = property(__default_length.value, __default_length.set, None, '\n                                                      Specify whether the spot should have a default length for this tag if the expected base cannot be matched.\n                                                  ')

    
    # Attribute base_coord uses Python identifier base_coord
    __base_coord = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'base_coord'), 'base_coord', '__SRA_common_CTD_ANON_5_base_coord', pyxb.binding.datatypes.nonNegativeInteger)
    __base_coord._DeclarationLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 530, 48)
    __base_coord._UseLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 530, 48)
    
    base_coord = property(__base_coord.value, __base_coord.set, None, '\n                                                      Specify an optional starting point for tag (base offset from 1).  \n                                                  ')

    _ElementMap.update({
        __BASECALL.name() : __BASECALL
    })
    _AttributeMap.update({
        __default_length.name() : __default_length,
        __base_coord.name() : __base_coord
    })
_module_typeBindings.CTD_ANON_5 = CTD_ANON_5


# Complex type {SRA.common}PlatformType with content type ELEMENT_ONLY
class PlatformType (pyxb.binding.basis.complexTypeDefinition):
    """ The PLATFORM record selects which sequencing platform and platform-specific runtime parameters. This will be
        determined by the Center. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PlatformType')
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 551, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element LS454 uses Python identifier LS454
    __LS454 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'LS454'), 'LS454', '__SRA_common_PlatformType_LS454', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 557, 12), )

    
    LS454 = property(__LS454.value, __LS454.set, None, ' 454 technology use 1-color sequential flows ')

    
    # Element ILLUMINA uses Python identifier ILLUMINA
    __ILLUMINA = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ILLUMINA'), 'ILLUMINA', '__SRA_common_PlatformType_ILLUMINA', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 568, 12), )

    
    ILLUMINA = property(__ILLUMINA.value, __ILLUMINA.set, None, ' Illumina is 4-channel flowgram with 1-to-1 mapping between basecalls and flows ')

    
    # Element HELICOS uses Python identifier HELICOS
    __HELICOS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'HELICOS'), 'HELICOS', '__SRA_common_PlatformType_HELICOS', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 579, 12), )

    
    HELICOS = property(__HELICOS.value, __HELICOS.set, None, ' Helicos is similar to 454 technology - uses 1-color sequential flows ')

    
    # Element ABI_SOLID uses Python identifier ABI_SOLID
    __ABI_SOLID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ABI_SOLID'), 'ABI_SOLID', '__SRA_common_PlatformType_ABI_SOLID', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 590, 12), )

    
    ABI_SOLID = property(__ABI_SOLID.value, __ABI_SOLID.set, None, ' ABI is 4-channel flowgram with 1-to-1 mapping between basecalls and flows ')

    
    # Element COMPLETE_GENOMICS uses Python identifier COMPLETE_GENOMICS
    __COMPLETE_GENOMICS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'COMPLETE_GENOMICS'), 'COMPLETE_GENOMICS', '__SRA_common_PlatformType_COMPLETE_GENOMICS', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 601, 12), )

    
    COMPLETE_GENOMICS = property(__COMPLETE_GENOMICS.value, __COMPLETE_GENOMICS.set, None, ' CompleteGenomics platform type. At present there is no instrument model. ')

    
    # Element BGISEQ uses Python identifier BGISEQ
    __BGISEQ = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'BGISEQ'), 'BGISEQ', '__SRA_common_PlatformType_BGISEQ', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 612, 12), )

    
    BGISEQ = property(__BGISEQ.value, __BGISEQ.set, None, '')

    
    # Element OXFORD_NANOPORE uses Python identifier OXFORD_NANOPORE
    __OXFORD_NANOPORE = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'OXFORD_NANOPORE'), 'OXFORD_NANOPORE', '__SRA_common_PlatformType_OXFORD_NANOPORE', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 623, 12), )

    
    OXFORD_NANOPORE = property(__OXFORD_NANOPORE.value, __OXFORD_NANOPORE.set, None, ' Oxford Nanopore platform type. nanopore-based electronic single molecule analysis ')

    
    # Element PACBIO_SMRT uses Python identifier PACBIO_SMRT
    __PACBIO_SMRT = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'PACBIO_SMRT'), 'PACBIO_SMRT', '__SRA_common_PlatformType_PACBIO_SMRT', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 634, 12), )

    
    PACBIO_SMRT = property(__PACBIO_SMRT.value, __PACBIO_SMRT.set, None, ' PacificBiosciences platform type for the single molecule real time (SMRT) technology. ')

    
    # Element ION_TORRENT uses Python identifier ION_TORRENT
    __ION_TORRENT = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ION_TORRENT'), 'ION_TORRENT', '__SRA_common_PlatformType_ION_TORRENT', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 645, 12), )

    
    ION_TORRENT = property(__ION_TORRENT.value, __ION_TORRENT.set, None, ' Ion Torrent Personal Genome Machine (PGM) from Life Technologies. ')

    
    # Element CAPILLARY uses Python identifier CAPILLARY
    __CAPILLARY = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'CAPILLARY'), 'CAPILLARY', '__SRA_common_PlatformType_CAPILLARY', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 656, 12), )

    
    CAPILLARY = property(__CAPILLARY.value, __CAPILLARY.set, None, ' Sequencers based on capillary electrophoresis technology manufactured by LifeTech (formerly Applied\n                BioSciences). ')

    _ElementMap.update({
        __LS454.name() : __LS454,
        __ILLUMINA.name() : __ILLUMINA,
        __HELICOS.name() : __HELICOS,
        __ABI_SOLID.name() : __ABI_SOLID,
        __COMPLETE_GENOMICS.name() : __COMPLETE_GENOMICS,
        __BGISEQ.name() : __BGISEQ,
        __OXFORD_NANOPORE.name() : __OXFORD_NANOPORE,
        __PACBIO_SMRT.name() : __PACBIO_SMRT,
        __ION_TORRENT.name() : __ION_TORRENT,
        __CAPILLARY.name() : __CAPILLARY
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.PlatformType = PlatformType
Namespace.addCategoryObject('typeBinding', 'PlatformType', PlatformType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_6 (pyxb.binding.basis.complexTypeDefinition):
    """ 454 technology use 1-color sequential flows """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 561, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element INSTRUMENT_MODEL uses Python identifier INSTRUMENT_MODEL
    __INSTRUMENT_MODEL = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'INSTRUMENT_MODEL'), 'INSTRUMENT_MODEL', '__SRA_common_CTD_ANON_6_INSTRUMENT_MODEL', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 563, 24), )

    
    INSTRUMENT_MODEL = property(__INSTRUMENT_MODEL.value, __INSTRUMENT_MODEL.set, None, None)

    _ElementMap.update({
        __INSTRUMENT_MODEL.name() : __INSTRUMENT_MODEL
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_6 = CTD_ANON_6


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_7 (pyxb.binding.basis.complexTypeDefinition):
    """ Illumina is 4-channel flowgram with 1-to-1 mapping between basecalls and flows """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 572, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element INSTRUMENT_MODEL uses Python identifier INSTRUMENT_MODEL
    __INSTRUMENT_MODEL = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'INSTRUMENT_MODEL'), 'INSTRUMENT_MODEL', '__SRA_common_CTD_ANON_7_INSTRUMENT_MODEL', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 574, 24), )

    
    INSTRUMENT_MODEL = property(__INSTRUMENT_MODEL.value, __INSTRUMENT_MODEL.set, None, None)

    _ElementMap.update({
        __INSTRUMENT_MODEL.name() : __INSTRUMENT_MODEL
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_7 = CTD_ANON_7


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_8 (pyxb.binding.basis.complexTypeDefinition):
    """ Helicos is similar to 454 technology - uses 1-color sequential flows """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 583, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element INSTRUMENT_MODEL uses Python identifier INSTRUMENT_MODEL
    __INSTRUMENT_MODEL = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'INSTRUMENT_MODEL'), 'INSTRUMENT_MODEL', '__SRA_common_CTD_ANON_8_INSTRUMENT_MODEL', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 585, 24), )

    
    INSTRUMENT_MODEL = property(__INSTRUMENT_MODEL.value, __INSTRUMENT_MODEL.set, None, None)

    _ElementMap.update({
        __INSTRUMENT_MODEL.name() : __INSTRUMENT_MODEL
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_8 = CTD_ANON_8


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_9 (pyxb.binding.basis.complexTypeDefinition):
    """ ABI is 4-channel flowgram with 1-to-1 mapping between basecalls and flows """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 594, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element INSTRUMENT_MODEL uses Python identifier INSTRUMENT_MODEL
    __INSTRUMENT_MODEL = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'INSTRUMENT_MODEL'), 'INSTRUMENT_MODEL', '__SRA_common_CTD_ANON_9_INSTRUMENT_MODEL', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 596, 24), )

    
    INSTRUMENT_MODEL = property(__INSTRUMENT_MODEL.value, __INSTRUMENT_MODEL.set, None, None)

    _ElementMap.update({
        __INSTRUMENT_MODEL.name() : __INSTRUMENT_MODEL
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_9 = CTD_ANON_9


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_10 (pyxb.binding.basis.complexTypeDefinition):
    """ CompleteGenomics platform type. At present there is no instrument model. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 605, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element INSTRUMENT_MODEL uses Python identifier INSTRUMENT_MODEL
    __INSTRUMENT_MODEL = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'INSTRUMENT_MODEL'), 'INSTRUMENT_MODEL', '__SRA_common_CTD_ANON_10_INSTRUMENT_MODEL', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 607, 24), )

    
    INSTRUMENT_MODEL = property(__INSTRUMENT_MODEL.value, __INSTRUMENT_MODEL.set, None, None)

    _ElementMap.update({
        __INSTRUMENT_MODEL.name() : __INSTRUMENT_MODEL
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_10 = CTD_ANON_10


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_11 (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 616, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element INSTRUMENT_MODEL uses Python identifier INSTRUMENT_MODEL
    __INSTRUMENT_MODEL = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'INSTRUMENT_MODEL'), 'INSTRUMENT_MODEL', '__SRA_common_CTD_ANON_11_INSTRUMENT_MODEL', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 618, 24), )

    
    INSTRUMENT_MODEL = property(__INSTRUMENT_MODEL.value, __INSTRUMENT_MODEL.set, None, None)

    _ElementMap.update({
        __INSTRUMENT_MODEL.name() : __INSTRUMENT_MODEL
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_11 = CTD_ANON_11


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_12 (pyxb.binding.basis.complexTypeDefinition):
    """ Oxford Nanopore platform type. nanopore-based electronic single molecule analysis """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 627, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element INSTRUMENT_MODEL uses Python identifier INSTRUMENT_MODEL
    __INSTRUMENT_MODEL = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'INSTRUMENT_MODEL'), 'INSTRUMENT_MODEL', '__SRA_common_CTD_ANON_12_INSTRUMENT_MODEL', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 629, 24), )

    
    INSTRUMENT_MODEL = property(__INSTRUMENT_MODEL.value, __INSTRUMENT_MODEL.set, None, None)

    _ElementMap.update({
        __INSTRUMENT_MODEL.name() : __INSTRUMENT_MODEL
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_12 = CTD_ANON_12


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_13 (pyxb.binding.basis.complexTypeDefinition):
    """ PacificBiosciences platform type for the single molecule real time (SMRT) technology. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 638, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element INSTRUMENT_MODEL uses Python identifier INSTRUMENT_MODEL
    __INSTRUMENT_MODEL = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'INSTRUMENT_MODEL'), 'INSTRUMENT_MODEL', '__SRA_common_CTD_ANON_13_INSTRUMENT_MODEL', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 640, 24), )

    
    INSTRUMENT_MODEL = property(__INSTRUMENT_MODEL.value, __INSTRUMENT_MODEL.set, None, None)

    _ElementMap.update({
        __INSTRUMENT_MODEL.name() : __INSTRUMENT_MODEL
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_13 = CTD_ANON_13


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_14 (pyxb.binding.basis.complexTypeDefinition):
    """ Ion Torrent Personal Genome Machine (PGM) from Life Technologies. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 649, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element INSTRUMENT_MODEL uses Python identifier INSTRUMENT_MODEL
    __INSTRUMENT_MODEL = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'INSTRUMENT_MODEL'), 'INSTRUMENT_MODEL', '__SRA_common_CTD_ANON_14_INSTRUMENT_MODEL', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 651, 24), )

    
    INSTRUMENT_MODEL = property(__INSTRUMENT_MODEL.value, __INSTRUMENT_MODEL.set, None, None)

    _ElementMap.update({
        __INSTRUMENT_MODEL.name() : __INSTRUMENT_MODEL
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_14 = CTD_ANON_14


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_15 (pyxb.binding.basis.complexTypeDefinition):
    """ Sequencers based on capillary electrophoresis technology manufactured by LifeTech (formerly Applied
                BioSciences). """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 661, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element INSTRUMENT_MODEL uses Python identifier INSTRUMENT_MODEL
    __INSTRUMENT_MODEL = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'INSTRUMENT_MODEL'), 'INSTRUMENT_MODEL', '__SRA_common_CTD_ANON_15_INSTRUMENT_MODEL', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 663, 24), )

    
    INSTRUMENT_MODEL = property(__INSTRUMENT_MODEL.value, __INSTRUMENT_MODEL.set, None, None)

    _ElementMap.update({
        __INSTRUMENT_MODEL.name() : __INSTRUMENT_MODEL
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_15 = CTD_ANON_15


# Complex type {SRA.common}SequencingDirectivesType with content type ELEMENT_ONLY
class SequencingDirectivesType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {SRA.common}SequencingDirectivesType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SequencingDirectivesType')
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 672, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element SAMPLE_DEMUX_DIRECTIVE uses Python identifier SAMPLE_DEMUX_DIRECTIVE
    __SAMPLE_DEMUX_DIRECTIVE = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'SAMPLE_DEMUX_DIRECTIVE'), 'SAMPLE_DEMUX_DIRECTIVE', '__SRA_common_SequencingDirectivesType_SAMPLE_DEMUX_DIRECTIVE', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 674, 12), )

    
    SAMPLE_DEMUX_DIRECTIVE = property(__SAMPLE_DEMUX_DIRECTIVE.value, __SAMPLE_DEMUX_DIRECTIVE.set, None, '\n                        Tells the Archive who will execute the sample demultiplexing operation..\n                    ')

    _ElementMap.update({
        __SAMPLE_DEMUX_DIRECTIVE.name() : __SAMPLE_DEMUX_DIRECTIVE
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.SequencingDirectivesType = SequencingDirectivesType
Namespace.addCategoryObject('typeBinding', 'SequencingDirectivesType', SequencingDirectivesType)


# Complex type {SRA.common}PipelineType with content type ELEMENT_ONLY
class PipelineType (pyxb.binding.basis.complexTypeDefinition):
    """ The PipelineType identifies the sequence or tree of actions to
                process the sequencing data. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PipelineType')
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 705, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element PIPE_SECTION uses Python identifier PIPE_SECTION
    __PIPE_SECTION = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'PIPE_SECTION'), 'PIPE_SECTION', '__SRA_common_PipelineType_PIPE_SECTION', True, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 711, 12), )

    
    PIPE_SECTION = property(__PIPE_SECTION.value, __PIPE_SECTION.set, None, None)

    _ElementMap.update({
        __PIPE_SECTION.name() : __PIPE_SECTION
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.PipelineType = PipelineType
Namespace.addCategoryObject('typeBinding', 'PipelineType', PipelineType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_16 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 712, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element STEP_INDEX uses Python identifier STEP_INDEX
    __STEP_INDEX = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'STEP_INDEX'), 'STEP_INDEX', '__SRA_common_CTD_ANON_16_STEP_INDEX', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 714, 24), )

    
    STEP_INDEX = property(__STEP_INDEX.value, __STEP_INDEX.set, None, '\n                                    Lexically ordered  value that allows for the pipe section to be hierarchically ordered.  The float primitive data type is\n                                    used to allow for pipe sections to be inserted later on.\n                                ')

    
    # Element PREV_STEP_INDEX uses Python identifier PREV_STEP_INDEX
    __PREV_STEP_INDEX = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'PREV_STEP_INDEX'), 'PREV_STEP_INDEX', '__SRA_common_CTD_ANON_16_PREV_STEP_INDEX', True, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 722, 24), )

    
    PREV_STEP_INDEX = property(__PREV_STEP_INDEX.value, __PREV_STEP_INDEX.set, None, '\n                                    STEP_INDEX of the previous step in the workflow.  Set toNIL if the first pipe section.\n                                ')

    
    # Element PROGRAM uses Python identifier PROGRAM
    __PROGRAM = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'PROGRAM'), 'PROGRAM', '__SRA_common_CTD_ANON_16_PROGRAM', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 730, 24), )

    
    PROGRAM = property(__PROGRAM.value, __PROGRAM.set, None, '\n                                    Name of the program or process for primary analysis.   This may include a test or condition\n                                    that leads to branching in the workflow.\n                                ')

    
    # Element VERSION uses Python identifier VERSION
    __VERSION = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'VERSION'), 'VERSION', '__SRA_common_CTD_ANON_16_VERSION', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 738, 24), )

    
    VERSION = property(__VERSION.value, __VERSION.set, None, '\n                                    Version of the program or process for primary analysis. \n                                ')

    
    # Element NOTES uses Python identifier NOTES
    __NOTES = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'NOTES'), 'NOTES', '__SRA_common_CTD_ANON_16_NOTES', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 745, 24), )

    
    NOTES = property(__NOTES.value, __NOTES.set, None, '\n                                    Notes about the program or process for primary analysis. \n                                ')

    
    # Attribute section_name uses Python identifier section_name
    __section_name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'section_name'), 'section_name', '__SRA_common_CTD_ANON_16_section_name', pyxb.binding.datatypes.string)
    __section_name._DeclarationLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 753, 20)
    __section_name._UseLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 753, 20)
    
    section_name = property(__section_name.value, __section_name.set, None, '\n                                Name of the processing pipeline section.\n                            ')

    _ElementMap.update({
        __STEP_INDEX.name() : __STEP_INDEX,
        __PREV_STEP_INDEX.name() : __PREV_STEP_INDEX,
        __PROGRAM.name() : __PROGRAM,
        __VERSION.name() : __VERSION,
        __NOTES.name() : __NOTES
    })
    _AttributeMap.update({
        __section_name.name() : __section_name
    })
_module_typeBindings.CTD_ANON_16 = CTD_ANON_16


# Complex type {SRA.common}ReferenceAssemblyType with content type ELEMENT_ONLY
class ReferenceAssemblyType (pyxb.binding.basis.complexTypeDefinition):
    """Reference assembly details."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ReferenceAssemblyType')
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 764, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element STANDARD uses Python identifier STANDARD
    __STANDARD = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'STANDARD'), 'STANDARD', '__SRA_common_ReferenceAssemblyType_STANDARD', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 770, 12), )

    
    STANDARD = property(__STANDARD.value, __STANDARD.set, None, 'A standard genome assembly.\n                                                 ')

    
    # Element CUSTOM uses Python identifier CUSTOM
    __CUSTOM = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'CUSTOM'), 'CUSTOM', '__SRA_common_ReferenceAssemblyType_CUSTOM', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 790, 12), )

    
    CUSTOM = property(__CUSTOM.value, __CUSTOM.set, None, 'Other genome assembly.')

    _ElementMap.update({
        __STANDARD.name() : __STANDARD,
        __CUSTOM.name() : __CUSTOM
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ReferenceAssemblyType = ReferenceAssemblyType
Namespace.addCategoryObject('typeBinding', 'ReferenceAssemblyType', ReferenceAssemblyType)


# Complex type [anonymous] with content type EMPTY
class CTD_ANON_17 (pyxb.binding.basis.complexTypeDefinition):
    """A standard genome assembly.
                                                 """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 775, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute refname uses Python identifier refname
    __refname = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'refname'), 'refname', '__SRA_common_CTD_ANON_17_refname', pyxb.binding.datatypes.string)
    __refname._DeclarationLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 776, 20)
    __refname._UseLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 776, 20)
    
    refname = property(__refname.value, __refname.set, None, 'A recognized name for the genome assembly.')

    
    # Attribute accession uses Python identifier accession
    __accession = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'accession'), 'accession', '__SRA_common_CTD_ANON_17_accession', pyxb.binding.datatypes.token)
    __accession._DeclarationLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 781, 20)
    __accession._UseLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 781, 20)
    
    accession = property(__accession.value, __accession.set, None, 'Identifies the genome assembly\n                                using an accession number and a sequence version.\n                             ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __refname.name() : __refname,
        __accession.name() : __accession
    })
_module_typeBindings.CTD_ANON_17 = CTD_ANON_17


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_18 (pyxb.binding.basis.complexTypeDefinition):
    """Other genome assembly."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 794, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element DESCRIPTION uses Python identifier DESCRIPTION
    __DESCRIPTION = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'DESCRIPTION'), 'DESCRIPTION', '__SRA_common_CTD_ANON_18_DESCRIPTION', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 796, 24), )

    
    DESCRIPTION = property(__DESCRIPTION.value, __DESCRIPTION.set, None, 'Description of the genome\n                                                 assembly.')

    
    # Element URL_LINK uses Python identifier URL_LINK
    __URL_LINK = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'URL_LINK'), 'URL_LINK', '__SRA_common_CTD_ANON_18_URL_LINK', True, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 802, 24), )

    
    URL_LINK = property(__URL_LINK.value, __URL_LINK.set, None, 'A link to the genome\n                                                 assembly.')

    _ElementMap.update({
        __DESCRIPTION.name() : __DESCRIPTION,
        __URL_LINK.name() : __URL_LINK
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_18 = CTD_ANON_18


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_19 (pyxb.binding.basis.complexTypeDefinition):
    """A link to the genome
                                                 assembly."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 807, 28)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element LABEL uses Python identifier LABEL
    __LABEL = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'LABEL'), 'LABEL', '__SRA_common_CTD_ANON_19_LABEL', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 809, 36), )

    
    LABEL = property(__LABEL.value, __LABEL.set, None, ' Text label to display for the\n                                                 link. ')

    
    # Element URL uses Python identifier URL
    __URL = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'URL'), 'URL', '__SRA_common_CTD_ANON_19_URL', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 816, 36), )

    
    URL = property(__URL.value, __URL.set, None, ' The internet service link\n                                                 (file:, http:, ftp:, etc). ')

    _ElementMap.update({
        __LABEL.name() : __LABEL,
        __URL.name() : __URL
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_19 = CTD_ANON_19


# Complex type {SRA.common}ReferenceSequenceType with content type ELEMENT_ONLY
class ReferenceSequenceType (pyxb.binding.basis.complexTypeDefinition):
    """Reference assembly and sequence details.                              """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ReferenceSequenceType')
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 831, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element ASSEMBLY uses Python identifier ASSEMBLY
    __ASSEMBLY = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ASSEMBLY'), 'ASSEMBLY', '__SRA_common_ReferenceSequenceType_ASSEMBLY', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 836, 12), )

    
    ASSEMBLY = property(__ASSEMBLY.value, __ASSEMBLY.set, None, 'Reference assembly details.')

    
    # Element SEQUENCE uses Python identifier SEQUENCE
    __SEQUENCE = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'SEQUENCE'), 'SEQUENCE', '__SRA_common_ReferenceSequenceType_SEQUENCE', True, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 841, 12), )

    
    SEQUENCE = property(__SEQUENCE.value, __SEQUENCE.set, None, 'Reference sequence details.')

    _ElementMap.update({
        __ASSEMBLY.name() : __ASSEMBLY,
        __SEQUENCE.name() : __SEQUENCE
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ReferenceSequenceType = ReferenceSequenceType
Namespace.addCategoryObject('typeBinding', 'ReferenceSequenceType', ReferenceSequenceType)


# Complex type [anonymous] with content type EMPTY
class CTD_ANON_20 (pyxb.binding.basis.complexTypeDefinition):
    """Reference sequence details."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 845, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute refname uses Python identifier refname
    __refname = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'refname'), 'refname', '__SRA_common_CTD_ANON_20_refname', pyxb.binding.datatypes.string)
    __refname._DeclarationLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 846, 20)
    __refname._UseLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 846, 20)
    
    refname = property(__refname.value, __refname.set, None, 'A recognized name for the\n                                                 reference sequence.')

    
    # Attribute accession uses Python identifier accession
    __accession = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'accession'), 'accession', '__SRA_common_CTD_ANON_20_accession', pyxb.binding.datatypes.token)
    __accession._DeclarationLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 853, 20)
    __accession._UseLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 853, 20)
    
    accession = property(__accession.value, __accession.set, None, '  Accession.version with version being mandatory\n                                  ')

    
    # Attribute label uses Python identifier label
    __label = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'label'), 'label', '__SRA_common_CTD_ANON_20_label', pyxb.binding.datatypes.string)
    __label._DeclarationLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 862, 20)
    __label._UseLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 862, 20)
    
    label = property(__label.value, __label.set, None, ' This is how Reference Sequence is labeled in submission file(s). \n                                  It is equivalent to  SQ label in BAM. \n                                  Optional when submitted file uses INSDC accession.version')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __refname.name() : __refname,
        __accession.name() : __accession,
        __label.name() : __label
    })
_module_typeBindings.CTD_ANON_20 = CTD_ANON_20


# Complex type {SRA.common}ProcessingType with content type ELEMENT_ONLY
class ProcessingType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {SRA.common}ProcessingType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ProcessingType')
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 876, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element PIPELINE uses Python identifier PIPELINE
    __PIPELINE = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'PIPELINE'), 'PIPELINE', '__SRA_common_ProcessingType_PIPELINE', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 878, 12), )

    
    PIPELINE = property(__PIPELINE.value, __PIPELINE.set, None, ' Generic processing pipeline specification. ')

    
    # Element DIRECTIVES uses Python identifier DIRECTIVES
    __DIRECTIVES = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'DIRECTIVES'), 'DIRECTIVES', '__SRA_common_ProcessingType_DIRECTIVES', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 883, 12), )

    
    DIRECTIVES = property(__DIRECTIVES.value, __DIRECTIVES.set, None, ' Processing directives tell the Sequence Read Archive how to\n                        treat the input data, if any treatment is requested. ')

    _ElementMap.update({
        __PIPELINE.name() : __PIPELINE,
        __DIRECTIVES.name() : __DIRECTIVES
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ProcessingType = ProcessingType
Namespace.addCategoryObject('typeBinding', 'ProcessingType', ProcessingType)


# Complex type {SRA.common}QualifiedNameType with content type SIMPLE
class QualifiedNameType (NameType):
    """Complex type {SRA.common}QualifiedNameType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'QualifiedNameType')
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 150, 4)
    _ElementMap = NameType._ElementMap.copy()
    _AttributeMap = NameType._AttributeMap.copy()
    # Base type is NameType
    
    # Attribute label inherited from {SRA.common}NameType
    
    # Attribute namespace uses Python identifier namespace
    __namespace = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'namespace'), 'namespace', '__SRA_common_QualifiedNameType_namespace', pyxb.binding.datatypes.string, required=True)
    __namespace._DeclarationLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 153, 16)
    __namespace._UseLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 153, 16)
    
    namespace = property(__namespace.value, __namespace.set, None, 'A string value that constrains the domain of named\n                            identifiers (namespace). ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __namespace.name() : __namespace
    })
_module_typeBindings.QualifiedNameType = QualifiedNameType
Namespace.addCategoryObject('typeBinding', 'QualifiedNameType', QualifiedNameType)


# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_21 (pyxb.binding.basis.complexTypeDefinition):
    """
                                                       Element's body contains a basecall, attribute provide description of this read meaning as well as matching rules.
                                                  """
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 454, 50)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute read_group_tag uses Python identifier read_group_tag
    __read_group_tag = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'read_group_tag'), 'read_group_tag', '__SRA_common_CTD_ANON_21_read_group_tag', pyxb.binding.datatypes.string)
    __read_group_tag._DeclarationLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 457, 50)
    __read_group_tag._UseLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 457, 50)
    
    read_group_tag = property(__read_group_tag.value, __read_group_tag.set, None, '\n                                                       When match occurs, the read will be tagged with this group membership\n                                                  ')

    
    # Attribute min_match uses Python identifier min_match
    __min_match = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'min_match'), 'min_match', '__SRA_common_CTD_ANON_21_min_match', pyxb.binding.datatypes.nonNegativeInteger)
    __min_match._DeclarationLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 465, 50)
    __min_match._UseLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 465, 50)
    
    min_match = property(__min_match.value, __min_match.set, None, '\n                                                       Minimum number of matches to trigger identification.\n                                                  ')

    
    # Attribute max_mismatch uses Python identifier max_mismatch
    __max_mismatch = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'max_mismatch'), 'max_mismatch', '__SRA_common_CTD_ANON_21_max_mismatch', pyxb.binding.datatypes.nonNegativeInteger)
    __max_mismatch._DeclarationLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 473, 50)
    __max_mismatch._UseLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 473, 50)
    
    max_mismatch = property(__max_mismatch.value, __max_mismatch.set, None, '\n                                                       Maximum number of mismatches \n                                                   ')

    
    # Attribute match_edge uses Python identifier match_edge
    __match_edge = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'match_edge'), 'match_edge', '__SRA_common_CTD_ANON_21_match_edge', _module_typeBindings.STD_ANON_2)
    __match_edge._DeclarationLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 481, 50)
    __match_edge._UseLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 481, 50)
    
    match_edge = property(__match_edge.value, __match_edge.set, None, '\n                                                       Where the match should occur. Changes the rules on how min_match and max_mismatch are counted.                                                                                                          \n                                                  ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __read_group_tag.name() : __read_group_tag,
        __min_match.name() : __min_match,
        __max_mismatch.name() : __max_mismatch,
        __match_edge.name() : __match_edge
    })
_module_typeBindings.CTD_ANON_21 = CTD_ANON_21




ObjectType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'IDENTIFIERS'), IdentifierType, scope=ObjectType, location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 19, 12)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 19, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ObjectType._UseForTag(pyxb.namespace.ExpandedName(None, 'IDENTIFIERS')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 19, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ObjectType._Automaton = _BuildAutomaton()




RefObjectType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'IDENTIFIERS'), IdentifierType, scope=RefObjectType, location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 53, 12)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 53, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(RefObjectType._UseForTag(pyxb.namespace.ExpandedName(None, 'IDENTIFIERS')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 53, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
RefObjectType._Automaton = _BuildAutomaton_()




IdentifierType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'PRIMARY_ID'), NameType, scope=IdentifierType, documentation='A primary identifier in the INSDC namespace.', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 168, 12)))

IdentifierType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'SECONDARY_ID'), NameType, scope=IdentifierType, documentation='A secondary identifier in the INSDC namespace.', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 173, 12)))

IdentifierType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'EXTERNAL_ID'), QualifiedNameType, scope=IdentifierType, documentation='An identifer rom a public non-INSDC resource.', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 178, 12)))

IdentifierType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'SUBMITTER_ID'), QualifiedNameType, scope=IdentifierType, documentation='A submitter provided identifier.', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 184, 12)))

IdentifierType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'UUID'), NameType, scope=IdentifierType, documentation='A universally unique identifier that requires no namespace.', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 189, 12)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 168, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 173, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 178, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 184, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 189, 12))
    counters.add(cc_4)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(IdentifierType._UseForTag(pyxb.namespace.ExpandedName(None, 'PRIMARY_ID')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 168, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(IdentifierType._UseForTag(pyxb.namespace.ExpandedName(None, 'SECONDARY_ID')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 173, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(IdentifierType._UseForTag(pyxb.namespace.ExpandedName(None, 'EXTERNAL_ID')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 178, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(IdentifierType._UseForTag(pyxb.namespace.ExpandedName(None, 'SUBMITTER_ID')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 184, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(IdentifierType._UseForTag(pyxb.namespace.ExpandedName(None, 'UUID')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 189, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
IdentifierType._Automaton = _BuildAutomaton_2()




XRefType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'DB'), pyxb.binding.datatypes.string, scope=XRefType, documentation=' INSDC controlled vocabulary of permitted cross references.\n                        Please see http://www.insdc.org/db_xref.html . For example, FLYBASE. ', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 198, 12)))

XRefType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ID'), pyxb.binding.datatypes.string, scope=XRefType, documentation='\n                            Accession in the referenced database.    For example,  FBtr0080008 (in FLYBASE).\n                        ', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 204, 12)))

XRefType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'LABEL'), pyxb.binding.datatypes.string, scope=XRefType, documentation='\n                            Text label to display for the link.\n                        ', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 211, 12)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(XRefType._UseForTag(pyxb.namespace.ExpandedName(None, 'DB')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 198, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=st_0)

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(XRefType._UseForTag(pyxb.namespace.ExpandedName(None, 'ID')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 204, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=st_0)

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 211, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(XRefType._UseForTag(pyxb.namespace.ExpandedName(None, 'LABEL')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 211, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 211, 12))
    counters.add(cc_0)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_4())
    sub_automata.append(_BuildAutomaton_5())
    sub_automata.append(_BuildAutomaton_6())
    final_update = set()
    symbol = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 197, 8)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
XRefType._Automaton = _BuildAutomaton_3()




URLType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'LABEL'), pyxb.binding.datatypes.string, scope=URLType, documentation='\n                        Text label to display for the link.\n                    ', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 223, 12)))

URLType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'URL'), pyxb.binding.datatypes.anyURI, scope=URLType, documentation='\n                        The internet service link (file:, http:, ftp:, etc).\n                    ', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 230, 12)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(URLType._UseForTag(pyxb.namespace.ExpandedName(None, 'LABEL')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 223, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=st_0)

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(URLType._UseForTag(pyxb.namespace.ExpandedName(None, 'URL')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 230, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=st_0)

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_8())
    sub_automata.append(_BuildAutomaton_9())
    final_update = set()
    symbol = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 222, 8)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
URLType._Automaton = _BuildAutomaton_7()




AttributeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'TAG'), pyxb.binding.datatypes.string, scope=AttributeType, documentation='\n                        Name of the attribute.\n                    ', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 246, 12)))

AttributeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'VALUE'), pyxb.binding.datatypes.string, scope=AttributeType, documentation='\n                        Value of the attribute.\n                    ', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 253, 12)))

AttributeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'UNITS'), pyxb.binding.datatypes.string, scope=AttributeType, documentation='\n                        Optional scientific units.\n                    ', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 260, 12)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AttributeType._UseForTag(pyxb.namespace.ExpandedName(None, 'TAG')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 246, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=st_0)

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 253, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AttributeType._UseForTag(pyxb.namespace.ExpandedName(None, 'VALUE')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 253, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 260, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AttributeType._UseForTag(pyxb.namespace.ExpandedName(None, 'UNITS')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 260, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 253, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 260, 12))
    counters.add(cc_1)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_11())
    sub_automata.append(_BuildAutomaton_12())
    sub_automata.append(_BuildAutomaton_13())
    final_update = set()
    symbol = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 245, 8)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
AttributeType._Automaton = _BuildAutomaton_10()




LinkType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'URL_LINK'), CTD_ANON, scope=LinkType, location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 277, 12)))

LinkType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'XREF_LINK'), XRefType, scope=LinkType, location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 295, 12)))

LinkType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ENTREZ_LINK'), CTD_ANON_, scope=LinkType, location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 297, 12)))

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(LinkType._UseForTag(pyxb.namespace.ExpandedName(None, 'URL_LINK')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 277, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(LinkType._UseForTag(pyxb.namespace.ExpandedName(None, 'XREF_LINK')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 295, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(LinkType._UseForTag(pyxb.namespace.ExpandedName(None, 'ENTREZ_LINK')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 297, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
LinkType._Automaton = _BuildAutomaton_14()




CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'LABEL'), pyxb.binding.datatypes.string, scope=CTD_ANON, documentation='\n                                    Text label to display for the link.\n                                ', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 280, 24)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'URL'), pyxb.binding.datatypes.anyURI, scope=CTD_ANON, documentation=' The internet service link (file:, http:, ftp: etc). ', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 287, 24)))

def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'LABEL')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 280, 24))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=st_0)

def _BuildAutomaton_17 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'URL')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 287, 24))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=st_0)

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_16())
    sub_automata.append(_BuildAutomaton_17())
    final_update = set()
    symbol = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 279, 20)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton_15()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'DB'), pyxb.binding.datatypes.string, scope=CTD_ANON_, documentation='\n                                    NCBI controlled vocabulary of permitted cross references.  Please see http://www.ncbi.nlm.nih.gov/entrez/eutils/einfo.fcgi? .\n                                ', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 300, 24)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ID'), pyxb.binding.datatypes.nonNegativeInteger, scope=CTD_ANON_, documentation='\n                                        Numeric record id meaningful to the NCBI Entrez system.\n                                    ', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 308, 28)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'QUERY'), pyxb.binding.datatypes.string, scope=CTD_ANON_, documentation='\n                                        Accession string meaningful to the NCBI Entrez system.\n                                    ', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 316, 28)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'LABEL'), pyxb.binding.datatypes.string, scope=CTD_ANON_, documentation='\n                                    How to label the link.\n                                ', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 324, 24)))

def _BuildAutomaton_18 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 324, 24))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, 'DB')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 300, 24))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, 'ID')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 308, 28))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, 'QUERY')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 316, 28))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, 'LABEL')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 324, 24))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_18()




SpotDescriptorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'SPOT_DECODE_SPEC'), CTD_ANON_2, scope=SpotDescriptorType, location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 349, 12)))

def _BuildAutomaton_19 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_19
    del _BuildAutomaton_19
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SpotDescriptorType._UseForTag(pyxb.namespace.ExpandedName(None, 'SPOT_DECODE_SPEC')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 349, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
SpotDescriptorType._Automaton = _BuildAutomaton_19()




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'SPOT_LENGTH'), pyxb.binding.datatypes.nonNegativeInteger, scope=CTD_ANON_2, documentation=' Number of base/color calls, cycles, or flows per\n                                    spot (raw sequence length or flow length including all\n                                    application and technical tags and mate pairs, but not including\n                                    gap lengths). This value will be platform dependent, library\n                                    dependent, and possibly run dependent. Variable length platforms\n                                    will still have a constant flow/cycle length. ', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 352, 24)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'READ_SPEC'), CTD_ANON_3, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 363, 24)))

def _BuildAutomaton_20 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_20
    del _BuildAutomaton_20
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 352, 24))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(None, 'SPOT_LENGTH')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 352, 24))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(None, 'READ_SPEC')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 363, 24))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_2._Automaton = _BuildAutomaton_20()




CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'READ_INDEX'), pyxb.binding.datatypes.nonNegativeInteger, scope=CTD_ANON_3, documentation='READ_INDEX starts at 0 and is incrementally increased for each sequential READ_SPEC within a SPOT_DECODE_SPEC', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 366, 36)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'READ_LABEL'), pyxb.binding.datatypes.string, scope=CTD_ANON_3, documentation='READ_LABEL is a name for this tag, and can be used to on output to determine read name, for example F or R.', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 372, 36)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'READ_CLASS'), STD_ANON, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 378, 36)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'READ_TYPE'), STD_ANON_, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 386, 36), unicode_default='Forward'))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'RELATIVE_ORDER'), CTD_ANON_4, scope=CTD_ANON_3, documentation='\n                                                        The read is located beginning at the offset or cycle relative to another read.  \n                                                        This choice is appropriate for example when specifying a read\n                                                        that follows a variable length expected sequence(s).\n                                                    ', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 406, 40)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'BASE_COORD'), pyxb.binding.datatypes.integer, scope=CTD_ANON_3, documentation='\n                                                        The location of the read start in terms of base count (1 is beginning of spot).\n                                                    ', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 433, 40)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'EXPECTED_BASECALL_TABLE'), CTD_ANON_5, scope=CTD_ANON_3, documentation='\n                                                        A set of choices of expected basecalls for a current read. Read will be zero-length if none is found.\n                                                    ', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 440, 40)))

def _BuildAutomaton_21 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_21
    del _BuildAutomaton_21
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 372, 36))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(None, 'READ_INDEX')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 366, 36))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(None, 'READ_LABEL')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 372, 36))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(None, 'READ_CLASS')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 378, 36))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(None, 'READ_TYPE')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 386, 36))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(None, 'RELATIVE_ORDER')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 406, 40))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(None, 'BASE_COORD')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 433, 40))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(None, 'EXPECTED_BASECALL_TABLE')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 440, 40))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    st_4._set_transitionSet(transitions)
    transitions = []
    st_5._set_transitionSet(transitions)
    transitions = []
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_3._Automaton = _BuildAutomaton_21()




CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'BASECALL'), CTD_ANON_21, scope=CTD_ANON_5, documentation="\n                                                       Element's body contains a basecall, attribute provide description of this read meaning as well as matching rules.\n                                                  ", location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 448, 50)))

def _BuildAutomaton_22 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_22
    del _BuildAutomaton_22
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(None, 'BASECALL')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 448, 50))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_5._Automaton = _BuildAutomaton_22()




PlatformType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'LS454'), CTD_ANON_6, scope=PlatformType, documentation=' 454 technology use 1-color sequential flows ', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 557, 12)))

PlatformType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ILLUMINA'), CTD_ANON_7, scope=PlatformType, documentation=' Illumina is 4-channel flowgram with 1-to-1 mapping between basecalls and flows ', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 568, 12)))

PlatformType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'HELICOS'), CTD_ANON_8, scope=PlatformType, documentation=' Helicos is similar to 454 technology - uses 1-color sequential flows ', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 579, 12)))

PlatformType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ABI_SOLID'), CTD_ANON_9, scope=PlatformType, documentation=' ABI is 4-channel flowgram with 1-to-1 mapping between basecalls and flows ', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 590, 12)))

PlatformType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'COMPLETE_GENOMICS'), CTD_ANON_10, scope=PlatformType, documentation=' CompleteGenomics platform type. At present there is no instrument model. ', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 601, 12)))

PlatformType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'BGISEQ'), CTD_ANON_11, scope=PlatformType, documentation='', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 612, 12)))

PlatformType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'OXFORD_NANOPORE'), CTD_ANON_12, scope=PlatformType, documentation=' Oxford Nanopore platform type. nanopore-based electronic single molecule analysis ', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 623, 12)))

PlatformType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'PACBIO_SMRT'), CTD_ANON_13, scope=PlatformType, documentation=' PacificBiosciences platform type for the single molecule real time (SMRT) technology. ', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 634, 12)))

PlatformType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ION_TORRENT'), CTD_ANON_14, scope=PlatformType, documentation=' Ion Torrent Personal Genome Machine (PGM) from Life Technologies. ', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 645, 12)))

PlatformType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'CAPILLARY'), CTD_ANON_15, scope=PlatformType, documentation=' Sequencers based on capillary electrophoresis technology manufactured by LifeTech (formerly Applied\n                BioSciences). ', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 656, 12)))

def _BuildAutomaton_23 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_23
    del _BuildAutomaton_23
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(PlatformType._UseForTag(pyxb.namespace.ExpandedName(None, 'LS454')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 557, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(PlatformType._UseForTag(pyxb.namespace.ExpandedName(None, 'ILLUMINA')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 568, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(PlatformType._UseForTag(pyxb.namespace.ExpandedName(None, 'HELICOS')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 579, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(PlatformType._UseForTag(pyxb.namespace.ExpandedName(None, 'ABI_SOLID')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 590, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(PlatformType._UseForTag(pyxb.namespace.ExpandedName(None, 'COMPLETE_GENOMICS')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 601, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(PlatformType._UseForTag(pyxb.namespace.ExpandedName(None, 'BGISEQ')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 612, 12))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(PlatformType._UseForTag(pyxb.namespace.ExpandedName(None, 'OXFORD_NANOPORE')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 623, 12))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(PlatformType._UseForTag(pyxb.namespace.ExpandedName(None, 'PACBIO_SMRT')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 634, 12))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(PlatformType._UseForTag(pyxb.namespace.ExpandedName(None, 'ION_TORRENT')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 645, 12))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(PlatformType._UseForTag(pyxb.namespace.ExpandedName(None, 'CAPILLARY')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 656, 12))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    transitions = []
    st_4._set_transitionSet(transitions)
    transitions = []
    st_5._set_transitionSet(transitions)
    transitions = []
    st_6._set_transitionSet(transitions)
    transitions = []
    st_7._set_transitionSet(transitions)
    transitions = []
    st_8._set_transitionSet(transitions)
    transitions = []
    st_9._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
PlatformType._Automaton = _BuildAutomaton_23()




CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'INSTRUMENT_MODEL'), type454Model, scope=CTD_ANON_6, location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 563, 24)))

def _BuildAutomaton_24 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_24
    del _BuildAutomaton_24
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(None, 'INSTRUMENT_MODEL')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 563, 24))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_6._Automaton = _BuildAutomaton_24()




CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'INSTRUMENT_MODEL'), typeIlluminaModel, scope=CTD_ANON_7, location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 574, 24)))

def _BuildAutomaton_25 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_25
    del _BuildAutomaton_25
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(None, 'INSTRUMENT_MODEL')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 574, 24))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_7._Automaton = _BuildAutomaton_25()




CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'INSTRUMENT_MODEL'), typeHelicosModel, scope=CTD_ANON_8, location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 585, 24)))

def _BuildAutomaton_26 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_26
    del _BuildAutomaton_26
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(None, 'INSTRUMENT_MODEL')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 585, 24))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_8._Automaton = _BuildAutomaton_26()




CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'INSTRUMENT_MODEL'), typeAbiSolidModel, scope=CTD_ANON_9, location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 596, 24)))

def _BuildAutomaton_27 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_27
    del _BuildAutomaton_27
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(None, 'INSTRUMENT_MODEL')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 596, 24))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_9._Automaton = _BuildAutomaton_27()




CTD_ANON_10._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'INSTRUMENT_MODEL'), typeCGModel, scope=CTD_ANON_10, location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 607, 24)))

def _BuildAutomaton_28 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_28
    del _BuildAutomaton_28
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(None, 'INSTRUMENT_MODEL')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 607, 24))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_10._Automaton = _BuildAutomaton_28()




CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'INSTRUMENT_MODEL'), typeBGISEQModel, scope=CTD_ANON_11, location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 618, 24)))

def _BuildAutomaton_29 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_29
    del _BuildAutomaton_29
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(None, 'INSTRUMENT_MODEL')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 618, 24))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_11._Automaton = _BuildAutomaton_29()




CTD_ANON_12._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'INSTRUMENT_MODEL'), typeOxfordNanoporeModel, scope=CTD_ANON_12, location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 629, 24)))

def _BuildAutomaton_30 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_30
    del _BuildAutomaton_30
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(None, 'INSTRUMENT_MODEL')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 629, 24))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_12._Automaton = _BuildAutomaton_30()




CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'INSTRUMENT_MODEL'), typePacBioModel, scope=CTD_ANON_13, location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 640, 24)))

def _BuildAutomaton_31 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_31
    del _BuildAutomaton_31
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(None, 'INSTRUMENT_MODEL')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 640, 24))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_13._Automaton = _BuildAutomaton_31()




CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'INSTRUMENT_MODEL'), typeIontorrentModel, scope=CTD_ANON_14, location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 651, 24)))

def _BuildAutomaton_32 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_32
    del _BuildAutomaton_32
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(None, 'INSTRUMENT_MODEL')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 651, 24))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_14._Automaton = _BuildAutomaton_32()




CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'INSTRUMENT_MODEL'), typeCapillaryModel, scope=CTD_ANON_15, location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 663, 24)))

def _BuildAutomaton_33 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_33
    del _BuildAutomaton_33
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(None, 'INSTRUMENT_MODEL')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 663, 24))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_15._Automaton = _BuildAutomaton_33()




SequencingDirectivesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'SAMPLE_DEMUX_DIRECTIVE'), STD_ANON_3, scope=SequencingDirectivesType, documentation='\n                        Tells the Archive who will execute the sample demultiplexing operation..\n                    ', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 674, 12)))

def _BuildAutomaton_34 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_34
    del _BuildAutomaton_34
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 674, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SequencingDirectivesType._UseForTag(pyxb.namespace.ExpandedName(None, 'SAMPLE_DEMUX_DIRECTIVE')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 674, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
SequencingDirectivesType._Automaton = _BuildAutomaton_34()




PipelineType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'PIPE_SECTION'), CTD_ANON_16, scope=PipelineType, location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 711, 12)))

def _BuildAutomaton_35 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_35
    del _BuildAutomaton_35
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(PipelineType._UseForTag(pyxb.namespace.ExpandedName(None, 'PIPE_SECTION')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 711, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
PipelineType._Automaton = _BuildAutomaton_35()




CTD_ANON_16._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'STEP_INDEX'), pyxb.binding.datatypes.string, scope=CTD_ANON_16, documentation='\n                                    Lexically ordered  value that allows for the pipe section to be hierarchically ordered.  The float primitive data type is\n                                    used to allow for pipe sections to be inserted later on.\n                                ', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 714, 24)))

CTD_ANON_16._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'PREV_STEP_INDEX'), pyxb.binding.datatypes.string, nillable=pyxb.binding.datatypes.boolean(1), scope=CTD_ANON_16, documentation='\n                                    STEP_INDEX of the previous step in the workflow.  Set toNIL if the first pipe section.\n                                ', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 722, 24)))

CTD_ANON_16._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'PROGRAM'), pyxb.binding.datatypes.string, scope=CTD_ANON_16, documentation='\n                                    Name of the program or process for primary analysis.   This may include a test or condition\n                                    that leads to branching in the workflow.\n                                ', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 730, 24)))

CTD_ANON_16._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'VERSION'), pyxb.binding.datatypes.string, scope=CTD_ANON_16, documentation='\n                                    Version of the program or process for primary analysis. \n                                ', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 738, 24)))

CTD_ANON_16._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'NOTES'), pyxb.binding.datatypes.string, scope=CTD_ANON_16, documentation='\n                                    Notes about the program or process for primary analysis. \n                                ', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 745, 24)))

def _BuildAutomaton_36 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_36
    del _BuildAutomaton_36
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 745, 24))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_16._UseForTag(pyxb.namespace.ExpandedName(None, 'STEP_INDEX')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 714, 24))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_16._UseForTag(pyxb.namespace.ExpandedName(None, 'PREV_STEP_INDEX')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 722, 24))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_16._UseForTag(pyxb.namespace.ExpandedName(None, 'PROGRAM')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 730, 24))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_16._UseForTag(pyxb.namespace.ExpandedName(None, 'VERSION')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 738, 24))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_16._UseForTag(pyxb.namespace.ExpandedName(None, 'NOTES')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 745, 24))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_16._Automaton = _BuildAutomaton_36()




ReferenceAssemblyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'STANDARD'), CTD_ANON_17, scope=ReferenceAssemblyType, documentation='A standard genome assembly.\n                                                 ', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 770, 12)))

ReferenceAssemblyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'CUSTOM'), CTD_ANON_18, scope=ReferenceAssemblyType, documentation='Other genome assembly.', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 790, 12)))

def _BuildAutomaton_37 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_37
    del _BuildAutomaton_37
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ReferenceAssemblyType._UseForTag(pyxb.namespace.ExpandedName(None, 'STANDARD')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 770, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ReferenceAssemblyType._UseForTag(pyxb.namespace.ExpandedName(None, 'CUSTOM')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 790, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ReferenceAssemblyType._Automaton = _BuildAutomaton_37()




CTD_ANON_18._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'DESCRIPTION'), pyxb.binding.datatypes.string, scope=CTD_ANON_18, documentation='Description of the genome\n                                                 assembly.', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 796, 24)))

CTD_ANON_18._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'URL_LINK'), CTD_ANON_19, scope=CTD_ANON_18, documentation='A link to the genome\n                                                 assembly.', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 802, 24)))

def _BuildAutomaton_38 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_38
    del _BuildAutomaton_38
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 796, 24))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_18._UseForTag(pyxb.namespace.ExpandedName(None, 'DESCRIPTION')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 796, 24))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_18._UseForTag(pyxb.namespace.ExpandedName(None, 'URL_LINK')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 802, 24))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_18._Automaton = _BuildAutomaton_38()




CTD_ANON_19._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'LABEL'), pyxb.binding.datatypes.string, scope=CTD_ANON_19, documentation=' Text label to display for the\n                                                 link. ', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 809, 36)))

CTD_ANON_19._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'URL'), pyxb.binding.datatypes.anyURI, scope=CTD_ANON_19, documentation=' The internet service link\n                                                 (file:, http:, ftp:, etc). ', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 816, 36)))

def _BuildAutomaton_40 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_40
    del _BuildAutomaton_40
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 809, 36))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_19._UseForTag(pyxb.namespace.ExpandedName(None, 'LABEL')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 809, 36))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_41 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_41
    del _BuildAutomaton_41
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_19._UseForTag(pyxb.namespace.ExpandedName(None, 'URL')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 816, 36))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=st_0)

def _BuildAutomaton_39 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_39
    del _BuildAutomaton_39
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 809, 36))
    counters.add(cc_0)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_40())
    sub_automata.append(_BuildAutomaton_41())
    final_update = set()
    symbol = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 808, 32)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_19._Automaton = _BuildAutomaton_39()




ReferenceSequenceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ASSEMBLY'), ReferenceAssemblyType, scope=ReferenceSequenceType, documentation='Reference assembly details.', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 836, 12)))

ReferenceSequenceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'SEQUENCE'), CTD_ANON_20, scope=ReferenceSequenceType, documentation='Reference sequence details.', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 841, 12)))

def _BuildAutomaton_42 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_42
    del _BuildAutomaton_42
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 836, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 841, 12))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ReferenceSequenceType._UseForTag(pyxb.namespace.ExpandedName(None, 'ASSEMBLY')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 836, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ReferenceSequenceType._UseForTag(pyxb.namespace.ExpandedName(None, 'SEQUENCE')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 841, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ReferenceSequenceType._Automaton = _BuildAutomaton_42()




ProcessingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'PIPELINE'), PipelineType, scope=ProcessingType, documentation=' Generic processing pipeline specification. ', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 878, 12)))

ProcessingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'DIRECTIVES'), SequencingDirectivesType, scope=ProcessingType, documentation=' Processing directives tell the Sequence Read Archive how to\n                        treat the input data, if any treatment is requested. ', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 883, 12)))

def _BuildAutomaton_43 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_43
    del _BuildAutomaton_43
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 878, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 883, 12))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ProcessingType._UseForTag(pyxb.namespace.ExpandedName(None, 'PIPELINE')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 878, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ProcessingType._UseForTag(pyxb.namespace.ExpandedName(None, 'DIRECTIVES')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 883, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ProcessingType._Automaton = _BuildAutomaton_43()

