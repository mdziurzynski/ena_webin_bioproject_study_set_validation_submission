# ./SRA_experiment.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2019-06-06 19:25:12.595339 by PyXB version 1.2.6 using Python 3.6.7.final.0
# Namespace AbsentNamespace0

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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:09971cd6-8880-11e9-9350-b0c090509cda')

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
from schemas import _com as _ImportedBinding__com

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.CreateAbsentNamespace()
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


# Atomic simple type: typeLibraryStrategy
class typeLibraryStrategy (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Sequencing technique intended for this library."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'typeLibraryStrategy')
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 18, 2)
    _Documentation = 'Sequencing technique intended for this library.'
typeLibraryStrategy._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=typeLibraryStrategy, enum_prefix=None)
typeLibraryStrategy.WGS = typeLibraryStrategy._CF_enumeration.addEnumeration(unicode_value='WGS', tag='WGS')
typeLibraryStrategy.WGA = typeLibraryStrategy._CF_enumeration.addEnumeration(unicode_value='WGA', tag='WGA')
typeLibraryStrategy.WXS = typeLibraryStrategy._CF_enumeration.addEnumeration(unicode_value='WXS', tag='WXS')
typeLibraryStrategy.RNA_Seq = typeLibraryStrategy._CF_enumeration.addEnumeration(unicode_value='RNA-Seq', tag='RNA_Seq')
typeLibraryStrategy.ssRNA_seq = typeLibraryStrategy._CF_enumeration.addEnumeration(unicode_value='ssRNA-seq', tag='ssRNA_seq')
typeLibraryStrategy.miRNA_Seq = typeLibraryStrategy._CF_enumeration.addEnumeration(unicode_value='miRNA-Seq', tag='miRNA_Seq')
typeLibraryStrategy.ncRNA_Seq = typeLibraryStrategy._CF_enumeration.addEnumeration(unicode_value='ncRNA-Seq', tag='ncRNA_Seq')
typeLibraryStrategy.FL_cDNA = typeLibraryStrategy._CF_enumeration.addEnumeration(unicode_value='FL-cDNA', tag='FL_cDNA')
typeLibraryStrategy.EST = typeLibraryStrategy._CF_enumeration.addEnumeration(unicode_value='EST', tag='EST')
typeLibraryStrategy.Hi_C = typeLibraryStrategy._CF_enumeration.addEnumeration(unicode_value='Hi-C', tag='Hi_C')
typeLibraryStrategy.ATAC_seq = typeLibraryStrategy._CF_enumeration.addEnumeration(unicode_value='ATAC-seq', tag='ATAC_seq')
typeLibraryStrategy.WCS = typeLibraryStrategy._CF_enumeration.addEnumeration(unicode_value='WCS', tag='WCS')
typeLibraryStrategy.RAD_Seq = typeLibraryStrategy._CF_enumeration.addEnumeration(unicode_value='RAD-Seq', tag='RAD_Seq')
typeLibraryStrategy.CLONE = typeLibraryStrategy._CF_enumeration.addEnumeration(unicode_value='CLONE', tag='CLONE')
typeLibraryStrategy.POOLCLONE = typeLibraryStrategy._CF_enumeration.addEnumeration(unicode_value='POOLCLONE', tag='POOLCLONE')
typeLibraryStrategy.AMPLICON = typeLibraryStrategy._CF_enumeration.addEnumeration(unicode_value='AMPLICON', tag='AMPLICON')
typeLibraryStrategy.CLONEEND = typeLibraryStrategy._CF_enumeration.addEnumeration(unicode_value='CLONEEND', tag='CLONEEND')
typeLibraryStrategy.FINISHING = typeLibraryStrategy._CF_enumeration.addEnumeration(unicode_value='FINISHING', tag='FINISHING')
typeLibraryStrategy.ChIP_Seq = typeLibraryStrategy._CF_enumeration.addEnumeration(unicode_value='ChIP-Seq', tag='ChIP_Seq')
typeLibraryStrategy.MNase_Seq = typeLibraryStrategy._CF_enumeration.addEnumeration(unicode_value='MNase-Seq', tag='MNase_Seq')
typeLibraryStrategy.DNase_Hypersensitivity = typeLibraryStrategy._CF_enumeration.addEnumeration(unicode_value='DNase-Hypersensitivity', tag='DNase_Hypersensitivity')
typeLibraryStrategy.Bisulfite_Seq = typeLibraryStrategy._CF_enumeration.addEnumeration(unicode_value='Bisulfite-Seq', tag='Bisulfite_Seq')
typeLibraryStrategy.CTS = typeLibraryStrategy._CF_enumeration.addEnumeration(unicode_value='CTS', tag='CTS')
typeLibraryStrategy.MRE_Seq = typeLibraryStrategy._CF_enumeration.addEnumeration(unicode_value='MRE-Seq', tag='MRE_Seq')
typeLibraryStrategy.MeDIP_Seq = typeLibraryStrategy._CF_enumeration.addEnumeration(unicode_value='MeDIP-Seq', tag='MeDIP_Seq')
typeLibraryStrategy.MBD_Seq = typeLibraryStrategy._CF_enumeration.addEnumeration(unicode_value='MBD-Seq', tag='MBD_Seq')
typeLibraryStrategy.Tn_Seq = typeLibraryStrategy._CF_enumeration.addEnumeration(unicode_value='Tn-Seq', tag='Tn_Seq')
typeLibraryStrategy.VALIDATION = typeLibraryStrategy._CF_enumeration.addEnumeration(unicode_value='VALIDATION', tag='VALIDATION')
typeLibraryStrategy.FAIRE_seq = typeLibraryStrategy._CF_enumeration.addEnumeration(unicode_value='FAIRE-seq', tag='FAIRE_seq')
typeLibraryStrategy.SELEX = typeLibraryStrategy._CF_enumeration.addEnumeration(unicode_value='SELEX', tag='SELEX')
typeLibraryStrategy.RIP_Seq = typeLibraryStrategy._CF_enumeration.addEnumeration(unicode_value='RIP-Seq', tag='RIP_Seq')
typeLibraryStrategy.ChIA_PET = typeLibraryStrategy._CF_enumeration.addEnumeration(unicode_value='ChIA-PET', tag='ChIA_PET')
typeLibraryStrategy.Synthetic_Long_Read = typeLibraryStrategy._CF_enumeration.addEnumeration(unicode_value='Synthetic-Long-Read', tag='Synthetic_Long_Read')
typeLibraryStrategy.Targeted_Capture = typeLibraryStrategy._CF_enumeration.addEnumeration(unicode_value='Targeted-Capture', tag='Targeted_Capture')
typeLibraryStrategy.Tethered_Chromatin_Conformation_Capture = typeLibraryStrategy._CF_enumeration.addEnumeration(unicode_value='Tethered Chromatin Conformation Capture', tag='Tethered_Chromatin_Conformation_Capture')
typeLibraryStrategy.OTHER = typeLibraryStrategy._CF_enumeration.addEnumeration(unicode_value='OTHER', tag='OTHER')
typeLibraryStrategy._InitializeFacetMap(typeLibraryStrategy._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'typeLibraryStrategy', typeLibraryStrategy)
_module_typeBindings.typeLibraryStrategy = typeLibraryStrategy

# Atomic simple type: typeLibrarySource
class typeLibrarySource (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """ The LIBRARY_SOURCE specifies the type of source material that is being sequenced. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'typeLibrarySource')
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 210, 2)
    _Documentation = ' The LIBRARY_SOURCE specifies the type of source material that is being sequenced. '
typeLibrarySource._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=typeLibrarySource, enum_prefix=None)
typeLibrarySource.GENOMIC = typeLibrarySource._CF_enumeration.addEnumeration(unicode_value='GENOMIC', tag='GENOMIC')
typeLibrarySource.GENOMIC_SINGLE_CELL = typeLibrarySource._CF_enumeration.addEnumeration(unicode_value='GENOMIC SINGLE CELL', tag='GENOMIC_SINGLE_CELL')
typeLibrarySource.TRANSCRIPTOMIC = typeLibrarySource._CF_enumeration.addEnumeration(unicode_value='TRANSCRIPTOMIC', tag='TRANSCRIPTOMIC')
typeLibrarySource.TRANSCRIPTOMIC_SINGLE_CELL = typeLibrarySource._CF_enumeration.addEnumeration(unicode_value='TRANSCRIPTOMIC SINGLE CELL', tag='TRANSCRIPTOMIC_SINGLE_CELL')
typeLibrarySource.METAGENOMIC = typeLibrarySource._CF_enumeration.addEnumeration(unicode_value='METAGENOMIC', tag='METAGENOMIC')
typeLibrarySource.METATRANSCRIPTOMIC = typeLibrarySource._CF_enumeration.addEnumeration(unicode_value='METATRANSCRIPTOMIC', tag='METATRANSCRIPTOMIC')
typeLibrarySource.SYNTHETIC = typeLibrarySource._CF_enumeration.addEnumeration(unicode_value='SYNTHETIC', tag='SYNTHETIC')
typeLibrarySource.VIRAL_RNA = typeLibrarySource._CF_enumeration.addEnumeration(unicode_value='VIRAL RNA', tag='VIRAL_RNA')
typeLibrarySource.OTHER = typeLibrarySource._CF_enumeration.addEnumeration(unicode_value='OTHER', tag='OTHER')
typeLibrarySource._InitializeFacetMap(typeLibrarySource._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'typeLibrarySource', typeLibrarySource)
_module_typeBindings.typeLibrarySource = typeLibrarySource

# Atomic simple type: typeLibrarySelection
class typeLibrarySelection (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """ Method used to enrich the target in the sequence library preparation """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'typeLibrarySelection')
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 255, 2)
    _Documentation = ' Method used to enrich the target in the sequence library preparation '
typeLibrarySelection._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=typeLibrarySelection, enum_prefix=None)
typeLibrarySelection.RANDOM = typeLibrarySelection._CF_enumeration.addEnumeration(unicode_value='RANDOM', tag='RANDOM')
typeLibrarySelection.PCR = typeLibrarySelection._CF_enumeration.addEnumeration(unicode_value='PCR', tag='PCR')
typeLibrarySelection.RANDOM_PCR = typeLibrarySelection._CF_enumeration.addEnumeration(unicode_value='RANDOM PCR', tag='RANDOM_PCR')
typeLibrarySelection.RT_PCR = typeLibrarySelection._CF_enumeration.addEnumeration(unicode_value='RT-PCR', tag='RT_PCR')
typeLibrarySelection.HMPR = typeLibrarySelection._CF_enumeration.addEnumeration(unicode_value='HMPR', tag='HMPR')
typeLibrarySelection.MF = typeLibrarySelection._CF_enumeration.addEnumeration(unicode_value='MF', tag='MF')
typeLibrarySelection.repeat_fractionation = typeLibrarySelection._CF_enumeration.addEnumeration(unicode_value='repeat fractionation', tag='repeat_fractionation')
typeLibrarySelection.size_fractionation = typeLibrarySelection._CF_enumeration.addEnumeration(unicode_value='size fractionation', tag='size_fractionation')
typeLibrarySelection.MSLL = typeLibrarySelection._CF_enumeration.addEnumeration(unicode_value='MSLL', tag='MSLL')
typeLibrarySelection.cDNA = typeLibrarySelection._CF_enumeration.addEnumeration(unicode_value='cDNA', tag='cDNA')
typeLibrarySelection.cDNA_randomPriming = typeLibrarySelection._CF_enumeration.addEnumeration(unicode_value='cDNA_randomPriming', tag='cDNA_randomPriming')
typeLibrarySelection.cDNA_oligo_dT = typeLibrarySelection._CF_enumeration.addEnumeration(unicode_value='cDNA_oligo_dT', tag='cDNA_oligo_dT')
typeLibrarySelection.PolyA = typeLibrarySelection._CF_enumeration.addEnumeration(unicode_value='PolyA', tag='PolyA')
typeLibrarySelection.Oligo_dT = typeLibrarySelection._CF_enumeration.addEnumeration(unicode_value='Oligo-dT', tag='Oligo_dT')
typeLibrarySelection.Inverse_rRNA = typeLibrarySelection._CF_enumeration.addEnumeration(unicode_value='Inverse rRNA', tag='Inverse_rRNA')
typeLibrarySelection.Inverse_rRNA_selection = typeLibrarySelection._CF_enumeration.addEnumeration(unicode_value='Inverse rRNA selection', tag='Inverse_rRNA_selection')
typeLibrarySelection.ChIP = typeLibrarySelection._CF_enumeration.addEnumeration(unicode_value='ChIP', tag='ChIP')
typeLibrarySelection.ChIP_Seq = typeLibrarySelection._CF_enumeration.addEnumeration(unicode_value='ChIP-Seq', tag='ChIP_Seq')
typeLibrarySelection.MNase = typeLibrarySelection._CF_enumeration.addEnumeration(unicode_value='MNase', tag='MNase')
typeLibrarySelection.DNase = typeLibrarySelection._CF_enumeration.addEnumeration(unicode_value='DNase', tag='DNase')
typeLibrarySelection.Hybrid_Selection = typeLibrarySelection._CF_enumeration.addEnumeration(unicode_value='Hybrid Selection', tag='Hybrid_Selection')
typeLibrarySelection.Reduced_Representation = typeLibrarySelection._CF_enumeration.addEnumeration(unicode_value='Reduced Representation', tag='Reduced_Representation')
typeLibrarySelection.Restriction_Digest = typeLibrarySelection._CF_enumeration.addEnumeration(unicode_value='Restriction Digest', tag='Restriction_Digest')
typeLibrarySelection.n5_methylcytidine_antibody = typeLibrarySelection._CF_enumeration.addEnumeration(unicode_value='5-methylcytidine antibody', tag='n5_methylcytidine_antibody')
typeLibrarySelection.MBD2_protein_methyl_CpG_binding_domain = typeLibrarySelection._CF_enumeration.addEnumeration(unicode_value='MBD2 protein methyl-CpG binding domain', tag='MBD2_protein_methyl_CpG_binding_domain')
typeLibrarySelection.CAGE = typeLibrarySelection._CF_enumeration.addEnumeration(unicode_value='CAGE', tag='CAGE')
typeLibrarySelection.RACE = typeLibrarySelection._CF_enumeration.addEnumeration(unicode_value='RACE', tag='RACE')
typeLibrarySelection.MDA = typeLibrarySelection._CF_enumeration.addEnumeration(unicode_value='MDA', tag='MDA')
typeLibrarySelection.padlock_probes_capture_method = typeLibrarySelection._CF_enumeration.addEnumeration(unicode_value='padlock probes capture method', tag='padlock_probes_capture_method')
typeLibrarySelection.other = typeLibrarySelection._CF_enumeration.addEnumeration(unicode_value='other', tag='other')
typeLibrarySelection.unspecified = typeLibrarySelection._CF_enumeration.addEnumeration(unicode_value='unspecified', tag='unspecified')
typeLibrarySelection._InitializeFacetMap(typeLibrarySelection._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'typeLibrarySelection', typeLibrarySelection)
_module_typeBindings.typeLibrarySelection = typeLibrarySelection

# Atomic simple type: [anonymous]
class STD_ANON (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 548, 18)
    _Documentation = None
STD_ANON._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON, enum_prefix=None)
STD_ANON.n16S_rRNA = STD_ANON._CF_enumeration.addEnumeration(unicode_value='16S rRNA', tag='n16S_rRNA')
STD_ANON.n18S_rRNA = STD_ANON._CF_enumeration.addEnumeration(unicode_value='18S rRNA', tag='n18S_rRNA')
STD_ANON.RBCL = STD_ANON._CF_enumeration.addEnumeration(unicode_value='RBCL', tag='RBCL')
STD_ANON.matK = STD_ANON._CF_enumeration.addEnumeration(unicode_value='matK', tag='matK')
STD_ANON.COX1 = STD_ANON._CF_enumeration.addEnumeration(unicode_value='COX1', tag='COX1')
STD_ANON.ITS1_5_8S_ITS2 = STD_ANON._CF_enumeration.addEnumeration(unicode_value='ITS1-5.8S-ITS2', tag='ITS1_5_8S_ITS2')
STD_ANON.exome = STD_ANON._CF_enumeration.addEnumeration(unicode_value='exome', tag='exome')
STD_ANON.other = STD_ANON._CF_enumeration.addEnumeration(unicode_value='other', tag='other')
STD_ANON._InitializeFacetMap(STD_ANON._CF_enumeration)
_module_typeBindings.STD_ANON = STD_ANON

# Atomic simple type: [anonymous]
class STD_ANON_ (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 623, 8)
    _Documentation = None
STD_ANON_._InitializeFacetMap()
_module_typeBindings.STD_ANON_ = STD_ANON_

# Complex type [anonymous] with content type SIMPLE
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 422, 12)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute read_group_tag uses Python identifier read_group_tag
    __read_group_tag = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'read_group_tag'), 'read_group_tag', '__AbsentNamespace0_CTD_ANON_read_group_tag', pyxb.binding.datatypes.string)
    __read_group_tag._DeclarationLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 425, 18)
    __read_group_tag._UseLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 425, 18)
    
    read_group_tag = property(__read_group_tag.value, __read_group_tag.set, None, ' Assignment of read_group_tag to decoded read ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __read_group_tag.name() : __read_group_tag
    })
_module_typeBindings.CTD_ANON = CTD_ANON


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """
            Identifies a list of group/pool/multiplex sample members.  This implies that
            this sample record is a group, pool, or multiplex, but is continues to receive
            its own accession and can be referenced by an experiment.  By default if
            no match to any of the listed members can be determined, then the default
            sampel reference is used.
          """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 462, 12)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element DEFAULT_MEMBER uses Python identifier DEFAULT_MEMBER
    __DEFAULT_MEMBER = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'DEFAULT_MEMBER'), 'DEFAULT_MEMBER', '__AbsentNamespace0_CTD_ANON__DEFAULT_MEMBER', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 464, 16), )

    
    DEFAULT_MEMBER = property(__DEFAULT_MEMBER.value, __DEFAULT_MEMBER.set, None, ' Reference to the sample that is used when read membership cannot be determined. A default member should\n                  be provided if there exists a possibility that some reads will be left over from barcode/MID resolution. A default member\n                  is not needed when defining a true pool (where individual samples are not distinguished in the reads), or the reads have\n                  been partitioned among the pool members (no leftovers). ')

    
    # Element MEMBER uses Python identifier MEMBER
    __MEMBER = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'MEMBER'), 'MEMBER', '__AbsentNamespace0_CTD_ANON__MEMBER', True, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 472, 16), )

    
    MEMBER = property(__MEMBER.value, __MEMBER.set, None, ' Reference to the sample as determined from barcode/MID resolution or read partition. ')

    _ElementMap.update({
        __DEFAULT_MEMBER.name() : __DEFAULT_MEMBER,
        __MEMBER.name() : __MEMBER
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_ = CTD_ANON_


# Complex type LibraryDescriptorType with content type ELEMENT_ONLY
class LibraryDescriptorType (pyxb.binding.basis.complexTypeDefinition):
    """ The LIBRARY_DESCRIPTOR specifies the origin of the material being
        sequenced and any treatments that the material might have undergone that affect the
        sequencing result. This specification is needed even if the platform does not
        require a library construction step per se. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LibraryDescriptorType')
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 484, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element LIBRARY_NAME uses Python identifier LIBRARY_NAME
    __LIBRARY_NAME = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'LIBRARY_NAME'), 'LIBRARY_NAME', '__AbsentNamespace0_LibraryDescriptorType_LIBRARY_NAME', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 492, 6), )

    
    LIBRARY_NAME = property(__LIBRARY_NAME.value, __LIBRARY_NAME.set, None, "\n            The submitter's name for this library.\n          ")

    
    # Element LIBRARY_STRATEGY uses Python identifier LIBRARY_STRATEGY
    __LIBRARY_STRATEGY = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'LIBRARY_STRATEGY'), 'LIBRARY_STRATEGY', '__AbsentNamespace0_LibraryDescriptorType_LIBRARY_STRATEGY', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 499, 6), )

    
    LIBRARY_STRATEGY = property(__LIBRARY_STRATEGY.value, __LIBRARY_STRATEGY.set, None, None)

    
    # Element LIBRARY_SOURCE uses Python identifier LIBRARY_SOURCE
    __LIBRARY_SOURCE = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'LIBRARY_SOURCE'), 'LIBRARY_SOURCE', '__AbsentNamespace0_LibraryDescriptorType_LIBRARY_SOURCE', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 500, 6), )

    
    LIBRARY_SOURCE = property(__LIBRARY_SOURCE.value, __LIBRARY_SOURCE.set, None, None)

    
    # Element LIBRARY_SELECTION uses Python identifier LIBRARY_SELECTION
    __LIBRARY_SELECTION = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'LIBRARY_SELECTION'), 'LIBRARY_SELECTION', '__AbsentNamespace0_LibraryDescriptorType_LIBRARY_SELECTION', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 501, 6), )

    
    LIBRARY_SELECTION = property(__LIBRARY_SELECTION.value, __LIBRARY_SELECTION.set, None, None)

    
    # Element LIBRARY_LAYOUT uses Python identifier LIBRARY_LAYOUT
    __LIBRARY_LAYOUT = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'LIBRARY_LAYOUT'), 'LIBRARY_LAYOUT', '__AbsentNamespace0_LibraryDescriptorType_LIBRARY_LAYOUT', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 502, 6), )

    
    LIBRARY_LAYOUT = property(__LIBRARY_LAYOUT.value, __LIBRARY_LAYOUT.set, None, '\n            LIBRARY_LAYOUT specifies whether to expect single, paired, or other configuration of reads.\n            In the case of paired reads, information about the relative distance and orientation is specified.\n          ')

    
    # Element TARGETED_LOCI uses Python identifier TARGETED_LOCI
    __TARGETED_LOCI = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'TARGETED_LOCI'), 'TARGETED_LOCI', '__AbsentNamespace0_LibraryDescriptorType_TARGETED_LOCI', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 529, 6), )

    
    TARGETED_LOCI = property(__TARGETED_LOCI.value, __TARGETED_LOCI.set, None, None)

    
    # Element POOLING_STRATEGY uses Python identifier POOLING_STRATEGY
    __POOLING_STRATEGY = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'POOLING_STRATEGY'), 'POOLING_STRATEGY', '__AbsentNamespace0_LibraryDescriptorType_POOLING_STRATEGY', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 617, 6), )

    
    POOLING_STRATEGY = property(__POOLING_STRATEGY.value, __POOLING_STRATEGY.set, None, '\n            The optional pooling strategy indicates how the library or libraries are organized if multiple samples are involved.\n          ')

    
    # Element LIBRARY_CONSTRUCTION_PROTOCOL uses Python identifier LIBRARY_CONSTRUCTION_PROTOCOL
    __LIBRARY_CONSTRUCTION_PROTOCOL = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'LIBRARY_CONSTRUCTION_PROTOCOL'), 'LIBRARY_CONSTRUCTION_PROTOCOL', '__AbsentNamespace0_LibraryDescriptorType_LIBRARY_CONSTRUCTION_PROTOCOL', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 627, 6), )

    
    LIBRARY_CONSTRUCTION_PROTOCOL = property(__LIBRARY_CONSTRUCTION_PROTOCOL.value, __LIBRARY_CONSTRUCTION_PROTOCOL.set, None, '\n            Free form text describing the protocol by which the sequencing library was constructed.\n          ')

    _ElementMap.update({
        __LIBRARY_NAME.name() : __LIBRARY_NAME,
        __LIBRARY_STRATEGY.name() : __LIBRARY_STRATEGY,
        __LIBRARY_SOURCE.name() : __LIBRARY_SOURCE,
        __LIBRARY_SELECTION.name() : __LIBRARY_SELECTION,
        __LIBRARY_LAYOUT.name() : __LIBRARY_LAYOUT,
        __TARGETED_LOCI.name() : __TARGETED_LOCI,
        __POOLING_STRATEGY.name() : __POOLING_STRATEGY,
        __LIBRARY_CONSTRUCTION_PROTOCOL.name() : __LIBRARY_CONSTRUCTION_PROTOCOL
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.LibraryDescriptorType = LibraryDescriptorType
Namespace.addCategoryObject('typeBinding', 'LibraryDescriptorType', LibraryDescriptorType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """
            LIBRARY_LAYOUT specifies whether to expect single, paired, or other configuration of reads.
            In the case of paired reads, information about the relative distance and orientation is specified.
          """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 509, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element SINGLE uses Python identifier SINGLE
    __SINGLE = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'SINGLE'), 'SINGLE', '__AbsentNamespace0_CTD_ANON_2_SINGLE', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 511, 12), )

    
    SINGLE = property(__SINGLE.value, __SINGLE.set, None, None)

    
    # Element PAIRED uses Python identifier PAIRED
    __PAIRED = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'PAIRED'), 'PAIRED', '__AbsentNamespace0_CTD_ANON_2_PAIRED', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 520, 12), )

    
    PAIRED = property(__PAIRED.value, __PAIRED.set, None, None)

    _ElementMap.update({
        __SINGLE.name() : __SINGLE,
        __PAIRED.name() : __PAIRED
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_2 = CTD_ANON_2


# Complex type [anonymous] with content type EMPTY
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    """
                    Reads are unpaired (usual case).
                  """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 512, 14)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_3 = CTD_ANON_3


# Complex type [anonymous] with content type EMPTY
class CTD_ANON_4 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 521, 14)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute NOMINAL_LENGTH uses Python identifier NOMINAL_LENGTH
    __NOMINAL_LENGTH = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'NOMINAL_LENGTH'), 'NOMINAL_LENGTH', '__AbsentNamespace0_CTD_ANON_4_NOMINAL_LENGTH', pyxb.binding.datatypes.nonNegativeInteger)
    __NOMINAL_LENGTH._DeclarationLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 522, 16)
    __NOMINAL_LENGTH._UseLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 522, 16)
    
    NOMINAL_LENGTH = property(__NOMINAL_LENGTH.value, __NOMINAL_LENGTH.set, None, None)

    
    # Attribute NOMINAL_SDEV uses Python identifier NOMINAL_SDEV
    __NOMINAL_SDEV = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'NOMINAL_SDEV'), 'NOMINAL_SDEV', '__AbsentNamespace0_CTD_ANON_4_NOMINAL_SDEV', pyxb.binding.datatypes.double)
    __NOMINAL_SDEV._DeclarationLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 523, 16)
    __NOMINAL_SDEV._UseLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 523, 16)
    
    NOMINAL_SDEV = property(__NOMINAL_SDEV.value, __NOMINAL_SDEV.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __NOMINAL_LENGTH.name() : __NOMINAL_LENGTH,
        __NOMINAL_SDEV.name() : __NOMINAL_SDEV
    })
_module_typeBindings.CTD_ANON_4 = CTD_ANON_4


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_5 (pyxb.binding.basis.complexTypeDefinition):
    """
              Names the gene(s) or locus(loci) or other genomic feature(s) targeted by the sequence.
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 530, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element LOCUS uses Python identifier LOCUS
    __LOCUS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'LOCUS'), 'LOCUS', '__AbsentNamespace0_CTD_ANON_5_LOCUS', True, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 537, 12), )

    
    LOCUS = property(__LOCUS.value, __LOCUS.set, None, None)

    _ElementMap.update({
        __LOCUS.name() : __LOCUS
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_5 = CTD_ANON_5


# Complex type LibraryType with content type ELEMENT_ONLY
class LibraryType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type LibraryType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LibraryType')
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 636, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element DESIGN_DESCRIPTION uses Python identifier DESIGN_DESCRIPTION
    __DESIGN_DESCRIPTION = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'DESIGN_DESCRIPTION'), 'DESIGN_DESCRIPTION', '__AbsentNamespace0_LibraryType_DESIGN_DESCRIPTION', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 638, 6), )

    
    DESIGN_DESCRIPTION = property(__DESIGN_DESCRIPTION.value, __DESIGN_DESCRIPTION.set, None, 'Goal and setup of the individual library including library was constructed.')

    
    # Element SAMPLE_DESCRIPTOR uses Python identifier SAMPLE_DESCRIPTOR
    __SAMPLE_DESCRIPTOR = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'SAMPLE_DESCRIPTOR'), 'SAMPLE_DESCRIPTOR', '__AbsentNamespace0_LibraryType_SAMPLE_DESCRIPTOR', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 644, 6), )

    
    SAMPLE_DESCRIPTOR = property(__SAMPLE_DESCRIPTOR.value, __SAMPLE_DESCRIPTOR.set, None, ' Pick a sample to associate this experiment with. The sample may be an individual or a pool,\n            depending on how it is specified. ')

    
    # Element LIBRARY_DESCRIPTOR uses Python identifier LIBRARY_DESCRIPTOR
    __LIBRARY_DESCRIPTOR = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'LIBRARY_DESCRIPTOR'), 'LIBRARY_DESCRIPTOR', '__AbsentNamespace0_LibraryType_LIBRARY_DESCRIPTOR', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 651, 6), )

    
    LIBRARY_DESCRIPTOR = property(__LIBRARY_DESCRIPTOR.value, __LIBRARY_DESCRIPTOR.set, None, ' The LIBRARY_DESCRIPTOR specifies the origin of the material being sequenced and any\n            treatments that the material might have undergone that affect the sequencing result. This specification is\n            needed even if the platform does not require a library construction step per se. ')

    
    # Element SPOT_DESCRIPTOR uses Python identifier SPOT_DESCRIPTOR
    __SPOT_DESCRIPTOR = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'SPOT_DESCRIPTOR'), 'SPOT_DESCRIPTOR', '__AbsentNamespace0_LibraryType_SPOT_DESCRIPTOR', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 659, 6), )

    
    SPOT_DESCRIPTOR = property(__SPOT_DESCRIPTOR.value, __SPOT_DESCRIPTOR.set, None, ' The SPOT_DESCRIPTOR specifies how to decode the individual reads of interest from the\n            monolithic spot sequence. The spot descriptor contains aspects of the experimental design, platform, and\n            processing information. There will be two methods of specification: one will be an index into a table of\n            typical decodings, the other being an exact specification. This construct is needed for loading data and for\n            interpreting the loaded runs. It can be omitted if the loader can infer read layout (from multiple input\n            files or from one input files). ')

    _ElementMap.update({
        __DESIGN_DESCRIPTION.name() : __DESIGN_DESCRIPTION,
        __SAMPLE_DESCRIPTOR.name() : __SAMPLE_DESCRIPTOR,
        __LIBRARY_DESCRIPTOR.name() : __LIBRARY_DESCRIPTOR,
        __SPOT_DESCRIPTOR.name() : __SPOT_DESCRIPTOR
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.LibraryType = LibraryType
Namespace.addCategoryObject('typeBinding', 'LibraryType', LibraryType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_6 (pyxb.binding.basis.complexTypeDefinition):
    """
            Links to resources related to this experiment or experiment set (publication, datasets, online databases).
          """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 729, 12)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element EXPERIMENT_LINK uses Python identifier EXPERIMENT_LINK
    __EXPERIMENT_LINK = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'EXPERIMENT_LINK'), 'EXPERIMENT_LINK', '__AbsentNamespace0_CTD_ANON_6_EXPERIMENT_LINK', True, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 731, 16), )

    
    EXPERIMENT_LINK = property(__EXPERIMENT_LINK.value, __EXPERIMENT_LINK.set, None, None)

    _ElementMap.update({
        __EXPERIMENT_LINK.name() : __EXPERIMENT_LINK
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_6 = CTD_ANON_6


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_7 (pyxb.binding.basis.complexTypeDefinition):
    """
            Properties and attributes of the experiment.  These can be entered as free-form
            tag-value pairs.
          """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 743, 12)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element EXPERIMENT_ATTRIBUTE uses Python identifier EXPERIMENT_ATTRIBUTE
    __EXPERIMENT_ATTRIBUTE = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'EXPERIMENT_ATTRIBUTE'), 'EXPERIMENT_ATTRIBUTE', '__AbsentNamespace0_CTD_ANON_7_EXPERIMENT_ATTRIBUTE', True, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 745, 16), )

    
    EXPERIMENT_ATTRIBUTE = property(__EXPERIMENT_ATTRIBUTE.value, __EXPERIMENT_ATTRIBUTE.set, None, None)

    _ElementMap.update({
        __EXPERIMENT_ATTRIBUTE.name() : __EXPERIMENT_ATTRIBUTE
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_7 = CTD_ANON_7


# Complex type ExperimentSetType with content type ELEMENT_ONLY
class ExperimentSetType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type ExperimentSetType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ExperimentSetType')
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 754, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element EXPERIMENT uses Python identifier EXPERIMENT
    __EXPERIMENT = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'EXPERIMENT'), 'EXPERIMENT', '__AbsentNamespace0_ExperimentSetType_EXPERIMENT', True, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 756, 6), )

    
    EXPERIMENT = property(__EXPERIMENT.value, __EXPERIMENT.set, None, None)

    _ElementMap.update({
        __EXPERIMENT.name() : __EXPERIMENT
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ExperimentSetType = ExperimentSetType
Namespace.addCategoryObject('typeBinding', 'ExperimentSetType', ExperimentSetType)


# Complex type PoolMemberType with content type ELEMENT_ONLY
class PoolMemberType (_ImportedBinding__com.RefObjectType):
    """Complex type PoolMemberType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PoolMemberType')
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 417, 2)
    _ElementMap = _ImportedBinding__com.RefObjectType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__com.RefObjectType._AttributeMap.copy()
    # Base type is _ImportedBinding__com.RefObjectType
    
    # Element READ_LABEL uses Python identifier READ_LABEL
    __READ_LABEL = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'READ_LABEL'), 'READ_LABEL', '__AbsentNamespace0_PoolMemberType_READ_LABEL', True, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 421, 10), )

    
    READ_LABEL = property(__READ_LABEL.value, __READ_LABEL.set, None, None)

    
    # Element IDENTIFIERS (IDENTIFIERS) inherited from {SRA.common}RefObjectType
    
    # Attribute member_name uses Python identifier member_name
    __member_name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'member_name'), 'member_name', '__AbsentNamespace0_PoolMemberType_member_name', pyxb.binding.datatypes.string)
    __member_name._DeclarationLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 435, 8)
    __member_name._UseLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 435, 8)
    
    member_name = property(__member_name.value, __member_name.set, None, ' Label a sample within a scope of the pool ')

    
    # Attribute proportion uses Python identifier proportion
    __proportion = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'proportion'), 'proportion', '__AbsentNamespace0_PoolMemberType_proportion', pyxb.binding.datatypes.float)
    __proportion._DeclarationLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 440, 8)
    __proportion._UseLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 440, 8)
    
    proportion = property(__proportion.value, __proportion.set, None, ' Proportion of this sample (in percent) that was included in sample pool. ')

    
    # Attribute refname inherited from {SRA.common}RefObjectType
    
    # Attribute refcenter inherited from {SRA.common}RefObjectType
    
    # Attribute accession inherited from {SRA.common}RefObjectType
    _ElementMap.update({
        __READ_LABEL.name() : __READ_LABEL
    })
    _AttributeMap.update({
        __member_name.name() : __member_name,
        __proportion.name() : __proportion
    })
_module_typeBindings.PoolMemberType = PoolMemberType
Namespace.addCategoryObject('typeBinding', 'PoolMemberType', PoolMemberType)


# Complex type SampleDescriptorType with content type ELEMENT_ONLY
class SampleDescriptorType (_ImportedBinding__com.RefObjectType):
    """Complex type SampleDescriptorType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SampleDescriptorType')
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 448, 2)
    _ElementMap = _ImportedBinding__com.RefObjectType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__com.RefObjectType._AttributeMap.copy()
    # Base type is _ImportedBinding__com.RefObjectType
    
    # Element POOL uses Python identifier POOL
    __POOL = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'POOL'), 'POOL', '__AbsentNamespace0_SampleDescriptorType_POOL', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 452, 10), )

    
    POOL = property(__POOL.value, __POOL.set, None, '\n            Identifies a list of group/pool/multiplex sample members.  This implies that\n            this sample record is a group, pool, or multiplex, but is continues to receive\n            its own accession and can be referenced by an experiment.  By default if\n            no match to any of the listed members can be determined, then the default\n            sampel reference is used.\n          ')

    
    # Element IDENTIFIERS (IDENTIFIERS) inherited from {SRA.common}RefObjectType
    
    # Attribute refname inherited from {SRA.common}RefObjectType
    
    # Attribute refcenter inherited from {SRA.common}RefObjectType
    
    # Attribute accession inherited from {SRA.common}RefObjectType
    _ElementMap.update({
        __POOL.name() : __POOL
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.SampleDescriptorType = SampleDescriptorType
Namespace.addCategoryObject('typeBinding', 'SampleDescriptorType', SampleDescriptorType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_8 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 538, 14)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element PROBE_SET uses Python identifier PROBE_SET
    __PROBE_SET = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'PROBE_SET'), 'PROBE_SET', '__AbsentNamespace0_CTD_ANON_8_PROBE_SET', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 540, 18), )

    
    PROBE_SET = property(__PROBE_SET.value, __PROBE_SET.set, None, ' Reference to an archived primer or\n                        probe set. Example: dbProbe ')

    
    # Attribute locus_name uses Python identifier locus_name
    __locus_name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'locus_name'), 'locus_name', '__AbsentNamespace0_CTD_ANON_8_locus_name', _module_typeBindings.STD_ANON)
    __locus_name._DeclarationLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 547, 16)
    __locus_name._UseLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 547, 16)
    
    locus_name = property(__locus_name.value, __locus_name.set, None, None)

    
    # Attribute description uses Python identifier description
    __description = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'description'), 'description', '__AbsentNamespace0_CTD_ANON_8_description', pyxb.binding.datatypes.string)
    __description._DeclarationLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 603, 16)
    __description._UseLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 603, 16)
    
    description = property(__description.value, __description.set, None, ' Submitter supplied description of alternate locus and auxiliary\n                      information. ')

    _ElementMap.update({
        __PROBE_SET.name() : __PROBE_SET
    })
    _AttributeMap.update({
        __locus_name.name() : __locus_name,
        __description.name() : __description
    })
_module_typeBindings.CTD_ANON_8 = CTD_ANON_8


# Complex type ExperimentType with content type ELEMENT_ONLY
class ExperimentType (_ImportedBinding__com.ObjectType):
    """
        An Experiment specifies of what will be sequenced and how the sequencing will be performed.
        It does not contain results.
        An Experiment is composed of a design, a platform selection, and processing parameters.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ExperimentType')
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 673, 2)
    _ElementMap = _ImportedBinding__com.ObjectType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__com.ObjectType._AttributeMap.copy()
    # Base type is _ImportedBinding__com.ObjectType
    
    # Element TITLE uses Python identifier TITLE
    __TITLE = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'TITLE'), 'TITLE', '__AbsentNamespace0_ExperimentType_TITLE', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 686, 10), )

    
    TITLE = property(__TITLE.value, __TITLE.set, None, '\n            Short text that can be used to call out experiment records in searches or in displays.\n            This element is technically optional but should be used for all new records.\n          ')

    
    # Element STUDY_REF uses Python identifier STUDY_REF
    __STUDY_REF = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'STUDY_REF'), 'STUDY_REF', '__AbsentNamespace0_ExperimentType_STUDY_REF', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 694, 10), )

    
    STUDY_REF = property(__STUDY_REF.value, __STUDY_REF.set, None, '\n            Identifies the parent study.\n          ')

    
    # Element DESIGN uses Python identifier DESIGN
    __DESIGN = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'DESIGN'), 'DESIGN', '__AbsentNamespace0_ExperimentType_DESIGN', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 706, 10), )

    
    DESIGN = property(__DESIGN.value, __DESIGN.set, None, ' The library design including library properties, layout, protocol, targeting information, and spot and gap\n            descriptors. ')

    
    # Element PLATFORM uses Python identifier PLATFORM
    __PLATFORM = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'PLATFORM'), 'PLATFORM', '__AbsentNamespace0_ExperimentType_PLATFORM', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 712, 10), )

    
    PLATFORM = property(__PLATFORM.value, __PLATFORM.set, None, '\n            The PLATFORM record selects which sequencing platform and platform-specific runtime parameters.\n            This will be determined by the Center.\n          ')

    
    # Element PROCESSING uses Python identifier PROCESSING
    __PROCESSING = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'PROCESSING'), 'PROCESSING', '__AbsentNamespace0_ExperimentType_PROCESSING', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 721, 10), )

    
    PROCESSING = property(__PROCESSING.value, __PROCESSING.set, None, None)

    
    # Element EXPERIMENT_LINKS uses Python identifier EXPERIMENT_LINKS
    __EXPERIMENT_LINKS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'EXPERIMENT_LINKS'), 'EXPERIMENT_LINKS', '__AbsentNamespace0_ExperimentType_EXPERIMENT_LINKS', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 723, 10), )

    
    EXPERIMENT_LINKS = property(__EXPERIMENT_LINKS.value, __EXPERIMENT_LINKS.set, None, '\n            Links to resources related to this experiment or experiment set (publication, datasets, online databases).\n          ')

    
    # Element EXPERIMENT_ATTRIBUTES uses Python identifier EXPERIMENT_ATTRIBUTES
    __EXPERIMENT_ATTRIBUTES = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'EXPERIMENT_ATTRIBUTES'), 'EXPERIMENT_ATTRIBUTES', '__AbsentNamespace0_ExperimentType_EXPERIMENT_ATTRIBUTES', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 736, 10), )

    
    EXPERIMENT_ATTRIBUTES = property(__EXPERIMENT_ATTRIBUTES.value, __EXPERIMENT_ATTRIBUTES.set, None, '\n            Properties and attributes of the experiment.  These can be entered as free-form\n            tag-value pairs.\n          ')

    
    # Element IDENTIFIERS (IDENTIFIERS) inherited from {SRA.common}ObjectType
    
    # Attribute alias inherited from {SRA.common}ObjectType
    
    # Attribute center_name inherited from {SRA.common}ObjectType
    
    # Attribute broker_name inherited from {SRA.common}ObjectType
    
    # Attribute accession inherited from {SRA.common}ObjectType
    _ElementMap.update({
        __TITLE.name() : __TITLE,
        __STUDY_REF.name() : __STUDY_REF,
        __DESIGN.name() : __DESIGN,
        __PLATFORM.name() : __PLATFORM,
        __PROCESSING.name() : __PROCESSING,
        __EXPERIMENT_LINKS.name() : __EXPERIMENT_LINKS,
        __EXPERIMENT_ATTRIBUTES.name() : __EXPERIMENT_ATTRIBUTES
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ExperimentType = ExperimentType
Namespace.addCategoryObject('typeBinding', 'ExperimentType', ExperimentType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_9 (_ImportedBinding__com.RefObjectType):
    """
            Identifies the parent study.
          """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 700, 12)
    _ElementMap = _ImportedBinding__com.RefObjectType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__com.RefObjectType._AttributeMap.copy()
    # Base type is _ImportedBinding__com.RefObjectType
    
    # Element IDENTIFIERS (IDENTIFIERS) inherited from {SRA.common}RefObjectType
    
    # Attribute refname inherited from {SRA.common}RefObjectType
    
    # Attribute refcenter inherited from {SRA.common}RefObjectType
    
    # Attribute accession inherited from {SRA.common}RefObjectType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_9 = CTD_ANON_9


EXPERIMENT_SET = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EXPERIMENT_SET'), ExperimentSetType, documentation='\n        An EXPERMENT_SET is a container for a set of experiments and a common namespace.\n      ', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 760, 2))
Namespace.addCategoryObject('elementBinding', EXPERIMENT_SET.name().localName(), EXPERIMENT_SET)

EXPERIMENT = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EXPERIMENT'), ExperimentType, location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 769, 2))
Namespace.addCategoryObject('elementBinding', EXPERIMENT.name().localName(), EXPERIMENT)



CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'DEFAULT_MEMBER'), PoolMemberType, scope=CTD_ANON_, documentation=' Reference to the sample that is used when read membership cannot be determined. A default member should\n                  be provided if there exists a possibility that some reads will be left over from barcode/MID resolution. A default member\n                  is not needed when defining a true pool (where individual samples are not distinguished in the reads), or the reads have\n                  been partitioned among the pool members (no leftovers). ', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 464, 16)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'MEMBER'), PoolMemberType, scope=CTD_ANON_, documentation=' Reference to the sample as determined from barcode/MID resolution or read partition. ', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 472, 16)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 464, 16))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, 'DEFAULT_MEMBER')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 464, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, 'MEMBER')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 472, 16))
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
CTD_ANON_._Automaton = _BuildAutomaton()




LibraryDescriptorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'LIBRARY_NAME'), pyxb.binding.datatypes.string, scope=LibraryDescriptorType, documentation="\n            The submitter's name for this library.\n          ", location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 492, 6)))

LibraryDescriptorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'LIBRARY_STRATEGY'), typeLibraryStrategy, scope=LibraryDescriptorType, location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 499, 6)))

LibraryDescriptorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'LIBRARY_SOURCE'), typeLibrarySource, scope=LibraryDescriptorType, location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 500, 6)))

LibraryDescriptorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'LIBRARY_SELECTION'), typeLibrarySelection, scope=LibraryDescriptorType, location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 501, 6)))

LibraryDescriptorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'LIBRARY_LAYOUT'), CTD_ANON_2, scope=LibraryDescriptorType, documentation='\n            LIBRARY_LAYOUT specifies whether to expect single, paired, or other configuration of reads.\n            In the case of paired reads, information about the relative distance and orientation is specified.\n          ', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 502, 6)))

LibraryDescriptorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'TARGETED_LOCI'), CTD_ANON_5, scope=LibraryDescriptorType, location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 529, 6)))

LibraryDescriptorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'POOLING_STRATEGY'), STD_ANON_, scope=LibraryDescriptorType, documentation='\n            The optional pooling strategy indicates how the library or libraries are organized if multiple samples are involved.\n          ', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 617, 6)))

LibraryDescriptorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'LIBRARY_CONSTRUCTION_PROTOCOL'), pyxb.binding.datatypes.string, scope=LibraryDescriptorType, documentation='\n            Free form text describing the protocol by which the sequencing library was constructed.\n          ', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 627, 6)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 492, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 529, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 617, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 627, 6))
    counters.add(cc_3)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(LibraryDescriptorType._UseForTag(pyxb.namespace.ExpandedName(None, 'LIBRARY_NAME')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 492, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(LibraryDescriptorType._UseForTag(pyxb.namespace.ExpandedName(None, 'LIBRARY_STRATEGY')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 499, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(LibraryDescriptorType._UseForTag(pyxb.namespace.ExpandedName(None, 'LIBRARY_SOURCE')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 500, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(LibraryDescriptorType._UseForTag(pyxb.namespace.ExpandedName(None, 'LIBRARY_SELECTION')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 501, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(LibraryDescriptorType._UseForTag(pyxb.namespace.ExpandedName(None, 'LIBRARY_LAYOUT')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 502, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(LibraryDescriptorType._UseForTag(pyxb.namespace.ExpandedName(None, 'TARGETED_LOCI')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 529, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(LibraryDescriptorType._UseForTag(pyxb.namespace.ExpandedName(None, 'POOLING_STRATEGY')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 617, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(LibraryDescriptorType._UseForTag(pyxb.namespace.ExpandedName(None, 'LIBRARY_CONSTRUCTION_PROTOCOL')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 627, 6))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
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
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
LibraryDescriptorType._Automaton = _BuildAutomaton_()




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'SINGLE'), CTD_ANON_3, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 511, 12)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'PAIRED'), CTD_ANON_4, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 520, 12)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(None, 'SINGLE')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 511, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(None, 'PAIRED')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 520, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_2._Automaton = _BuildAutomaton_2()




CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'LOCUS'), CTD_ANON_8, scope=CTD_ANON_5, location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 537, 12)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(None, 'LOCUS')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 537, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_5._Automaton = _BuildAutomaton_3()




LibraryType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'DESIGN_DESCRIPTION'), pyxb.binding.datatypes.string, scope=LibraryType, documentation='Goal and setup of the individual library including library was constructed.', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 638, 6)))

LibraryType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'SAMPLE_DESCRIPTOR'), SampleDescriptorType, scope=LibraryType, documentation=' Pick a sample to associate this experiment with. The sample may be an individual or a pool,\n            depending on how it is specified. ', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 644, 6)))

LibraryType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'LIBRARY_DESCRIPTOR'), LibraryDescriptorType, scope=LibraryType, documentation=' The LIBRARY_DESCRIPTOR specifies the origin of the material being sequenced and any\n            treatments that the material might have undergone that affect the sequencing result. This specification is\n            needed even if the platform does not require a library construction step per se. ', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 651, 6)))

LibraryType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'SPOT_DESCRIPTOR'), _ImportedBinding__com.SpotDescriptorType, scope=LibraryType, documentation=' The SPOT_DESCRIPTOR specifies how to decode the individual reads of interest from the\n            monolithic spot sequence. The spot descriptor contains aspects of the experimental design, platform, and\n            processing information. There will be two methods of specification: one will be an index into a table of\n            typical decodings, the other being an exact specification. This construct is needed for loading data and for\n            interpreting the loaded runs. It can be omitted if the loader can infer read layout (from multiple input\n            files or from one input files). ', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 659, 6)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 659, 6))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(LibraryType._UseForTag(pyxb.namespace.ExpandedName(None, 'DESIGN_DESCRIPTION')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 638, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(LibraryType._UseForTag(pyxb.namespace.ExpandedName(None, 'SAMPLE_DESCRIPTOR')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 644, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(LibraryType._UseForTag(pyxb.namespace.ExpandedName(None, 'LIBRARY_DESCRIPTOR')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 651, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(LibraryType._UseForTag(pyxb.namespace.ExpandedName(None, 'SPOT_DESCRIPTOR')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 659, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
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
LibraryType._Automaton = _BuildAutomaton_4()




CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'EXPERIMENT_LINK'), _ImportedBinding__com.LinkType, scope=CTD_ANON_6, location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 731, 16)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(None, 'EXPERIMENT_LINK')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 731, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_6._Automaton = _BuildAutomaton_5()




CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'EXPERIMENT_ATTRIBUTE'), _ImportedBinding__com.AttributeType, scope=CTD_ANON_7, location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 745, 16)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(None, 'EXPERIMENT_ATTRIBUTE')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 745, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_7._Automaton = _BuildAutomaton_6()




ExperimentSetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'EXPERIMENT'), ExperimentType, scope=ExperimentSetType, location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 756, 6)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ExperimentSetType._UseForTag(pyxb.namespace.ExpandedName(None, 'EXPERIMENT')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 756, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ExperimentSetType._Automaton = _BuildAutomaton_7()




PoolMemberType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'READ_LABEL'), CTD_ANON, scope=PoolMemberType, location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 421, 10)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 53, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 421, 10))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(PoolMemberType._UseForTag(pyxb.namespace.ExpandedName(None, 'IDENTIFIERS')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 53, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(PoolMemberType._UseForTag(pyxb.namespace.ExpandedName(None, 'READ_LABEL')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 421, 10))
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
PoolMemberType._Automaton = _BuildAutomaton_8()




SampleDescriptorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'POOL'), CTD_ANON_, scope=SampleDescriptorType, documentation='\n            Identifies a list of group/pool/multiplex sample members.  This implies that\n            this sample record is a group, pool, or multiplex, but is continues to receive\n            its own accession and can be referenced by an experiment.  By default if\n            no match to any of the listed members can be determined, then the default\n            sampel reference is used.\n          ', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 452, 10)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 53, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 451, 8))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SampleDescriptorType._UseForTag(pyxb.namespace.ExpandedName(None, 'IDENTIFIERS')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 53, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(SampleDescriptorType._UseForTag(pyxb.namespace.ExpandedName(None, 'POOL')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 452, 10))
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
SampleDescriptorType._Automaton = _BuildAutomaton_9()




CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'PROBE_SET'), _ImportedBinding__com.XRefType, scope=CTD_ANON_8, documentation=' Reference to an archived primer or\n                        probe set. Example: dbProbe ', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 540, 18)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 540, 18))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(None, 'PROBE_SET')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 540, 18))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_8._Automaton = _BuildAutomaton_10()




ExperimentType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'TITLE'), pyxb.binding.datatypes.string, scope=ExperimentType, documentation='\n            Short text that can be used to call out experiment records in searches or in displays.\n            This element is technically optional but should be used for all new records.\n          ', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 686, 10)))

ExperimentType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'STUDY_REF'), CTD_ANON_9, scope=ExperimentType, documentation='\n            Identifies the parent study.\n          ', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 694, 10)))

ExperimentType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'DESIGN'), LibraryType, scope=ExperimentType, documentation=' The library design including library properties, layout, protocol, targeting information, and spot and gap\n            descriptors. ', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 706, 10)))

ExperimentType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'PLATFORM'), _ImportedBinding__com.PlatformType, scope=ExperimentType, documentation='\n            The PLATFORM record selects which sequencing platform and platform-specific runtime parameters.\n            This will be determined by the Center.\n          ', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 712, 10)))

ExperimentType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'PROCESSING'), _ImportedBinding__com.ProcessingType, scope=ExperimentType, location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 721, 10)))

ExperimentType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'EXPERIMENT_LINKS'), CTD_ANON_6, scope=ExperimentType, documentation='\n            Links to resources related to this experiment or experiment set (publication, datasets, online databases).\n          ', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 723, 10)))

ExperimentType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'EXPERIMENT_ATTRIBUTES'), CTD_ANON_7, scope=ExperimentType, documentation='\n            Properties and attributes of the experiment.  These can be entered as free-form\n            tag-value pairs.\n          ', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 736, 10)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 19, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 686, 10))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 721, 10))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 723, 10))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 736, 10))
    counters.add(cc_4)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ExperimentType._UseForTag(pyxb.namespace.ExpandedName(None, 'IDENTIFIERS')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 19, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ExperimentType._UseForTag(pyxb.namespace.ExpandedName(None, 'TITLE')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 686, 10))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ExperimentType._UseForTag(pyxb.namespace.ExpandedName(None, 'STUDY_REF')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 694, 10))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ExperimentType._UseForTag(pyxb.namespace.ExpandedName(None, 'DESIGN')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 706, 10))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ExperimentType._UseForTag(pyxb.namespace.ExpandedName(None, 'PLATFORM')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 712, 10))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(ExperimentType._UseForTag(pyxb.namespace.ExpandedName(None, 'PROCESSING')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 721, 10))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(ExperimentType._UseForTag(pyxb.namespace.ExpandedName(None, 'EXPERIMENT_LINKS')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 723, 10))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(ExperimentType._UseForTag(pyxb.namespace.ExpandedName(None, 'EXPERIMENT_ATTRIBUTES')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.experiment.xsd', 736, 10))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
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
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, True) ]))
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ExperimentType._Automaton = _BuildAutomaton_11()




def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 53, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(None, 'IDENTIFIERS')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 53, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_9._Automaton = _BuildAutomaton_12()

