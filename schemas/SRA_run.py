# ./SRA_run.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2019-06-06 19:25:15.570710 by PyXB version 1.2.6 using Python 3.6.7.final.0
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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:0b6aa8ac-8880-11e9-9350-b0c090509cda')

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


# Atomic simple type: [anonymous]
class STD_ANON (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.run.xsd', 98, 50)
    _Documentation = None
STD_ANON._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON, enum_prefix=None)
STD_ANON.sra = STD_ANON._CF_enumeration.addEnumeration(unicode_value='sra', tag='sra')
STD_ANON.srf = STD_ANON._CF_enumeration.addEnumeration(unicode_value='srf', tag='srf')
STD_ANON.sff = STD_ANON._CF_enumeration.addEnumeration(unicode_value='sff', tag='sff')
STD_ANON.fastq = STD_ANON._CF_enumeration.addEnumeration(unicode_value='fastq', tag='fastq')
STD_ANON.fasta = STD_ANON._CF_enumeration.addEnumeration(unicode_value='fasta', tag='fasta')
STD_ANON.tab = STD_ANON._CF_enumeration.addEnumeration(unicode_value='tab', tag='tab')
STD_ANON.n454_native = STD_ANON._CF_enumeration.addEnumeration(unicode_value='454_native', tag='n454_native')
STD_ANON.n454_native_seq = STD_ANON._CF_enumeration.addEnumeration(unicode_value='454_native_seq', tag='n454_native_seq')
STD_ANON.n454_native_qual = STD_ANON._CF_enumeration.addEnumeration(unicode_value='454_native_qual', tag='n454_native_qual')
STD_ANON.Helicos_native = STD_ANON._CF_enumeration.addEnumeration(unicode_value='Helicos_native', tag='Helicos_native')
STD_ANON.Illumina_native = STD_ANON._CF_enumeration.addEnumeration(unicode_value='Illumina_native', tag='Illumina_native')
STD_ANON.Illumina_native_seq = STD_ANON._CF_enumeration.addEnumeration(unicode_value='Illumina_native_seq', tag='Illumina_native_seq')
STD_ANON.Illumina_native_prb = STD_ANON._CF_enumeration.addEnumeration(unicode_value='Illumina_native_prb', tag='Illumina_native_prb')
STD_ANON.Illumina_native_int = STD_ANON._CF_enumeration.addEnumeration(unicode_value='Illumina_native_int', tag='Illumina_native_int')
STD_ANON.Illumina_native_qseq = STD_ANON._CF_enumeration.addEnumeration(unicode_value='Illumina_native_qseq', tag='Illumina_native_qseq')
STD_ANON.Illumina_native_scarf = STD_ANON._CF_enumeration.addEnumeration(unicode_value='Illumina_native_scarf', tag='Illumina_native_scarf')
STD_ANON.SOLiD_native = STD_ANON._CF_enumeration.addEnumeration(unicode_value='SOLiD_native', tag='SOLiD_native')
STD_ANON.SOLiD_native_csfasta = STD_ANON._CF_enumeration.addEnumeration(unicode_value='SOLiD_native_csfasta', tag='SOLiD_native_csfasta')
STD_ANON.SOLiD_native_qual = STD_ANON._CF_enumeration.addEnumeration(unicode_value='SOLiD_native_qual', tag='SOLiD_native_qual')
STD_ANON.PacBio_HDF5 = STD_ANON._CF_enumeration.addEnumeration(unicode_value='PacBio_HDF5', tag='PacBio_HDF5')
STD_ANON.bam = STD_ANON._CF_enumeration.addEnumeration(unicode_value='bam', tag='bam')
STD_ANON.cram = STD_ANON._CF_enumeration.addEnumeration(unicode_value='cram', tag='cram')
STD_ANON.CompleteGenomics_native = STD_ANON._CF_enumeration.addEnumeration(unicode_value='CompleteGenomics_native', tag='CompleteGenomics_native')
STD_ANON.OxfordNanopore_native = STD_ANON._CF_enumeration.addEnumeration(unicode_value='OxfordNanopore_native', tag='OxfordNanopore_native')
STD_ANON._InitializeFacetMap(STD_ANON._CF_enumeration)
_module_typeBindings.STD_ANON = STD_ANON

# Atomic simple type: [anonymous]
class STD_ANON_ (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.run.xsd', 328, 50)
    _Documentation = None
STD_ANON_._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_, enum_prefix=None)
STD_ANON_.phred = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='phred', tag='phred')
STD_ANON_.log_odds = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='log-odds', tag='log_odds')
STD_ANON_._InitializeFacetMap(STD_ANON_._CF_enumeration)
_module_typeBindings.STD_ANON_ = STD_ANON_

# Atomic simple type: [anonymous]
class STD_ANON_2 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.run.xsd', 359, 50)
    _Documentation = None
STD_ANON_2._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_2, enum_prefix=None)
STD_ANON_2.ascii = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='ascii', tag='ascii')
STD_ANON_2.decimal = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='decimal', tag='decimal')
STD_ANON_2.hexadecimal = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='hexadecimal', tag='hexadecimal')
STD_ANON_2._InitializeFacetMap(STD_ANON_2._CF_enumeration)
_module_typeBindings.STD_ANON_2 = STD_ANON_2

# Atomic simple type: [anonymous]
class STD_ANON_3 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.run.xsd', 391, 50)
    _Documentation = None
STD_ANON_3._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_3, enum_prefix=None)
STD_ANON_3.emptyString = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='!', tag='emptyString')
STD_ANON_3.emptyString_ = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='@', tag='emptyString_')
STD_ANON_3._InitializeFacetMap(STD_ANON_3._CF_enumeration)
_module_typeBindings.STD_ANON_3 = STD_ANON_3

# Atomic simple type: [anonymous]
class STD_ANON_4 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.run.xsd', 418, 50)
    _Documentation = None
STD_ANON_4._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_4, enum_prefix=None)
STD_ANON_4.MD5 = STD_ANON_4._CF_enumeration.addEnumeration(unicode_value='MD5', tag='MD5')
STD_ANON_4.SHA_256 = STD_ANON_4._CF_enumeration.addEnumeration(unicode_value='SHA-256', tag='SHA_256')
STD_ANON_4._InitializeFacetMap(STD_ANON_4._CF_enumeration)
_module_typeBindings.STD_ANON_4 = STD_ANON_4

# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """The type of the run. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.run.xsd', 57, 24)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element REFERENCE_ALIGNMENT uses Python identifier REFERENCE_ALIGNMENT
    __REFERENCE_ALIGNMENT = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'REFERENCE_ALIGNMENT'), 'REFERENCE_ALIGNMENT', '__AbsentNamespace0_CTD_ANON_REFERENCE_ALIGNMENT', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.run.xsd', 59, 32), )

    
    REFERENCE_ALIGNMENT = property(__REFERENCE_ALIGNMENT.value, __REFERENCE_ALIGNMENT.set, None, None)

    _ElementMap.update({
        __REFERENCE_ALIGNMENT.name() : __REFERENCE_ALIGNMENT
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
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.run.xsd', 67, 28)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element FILES uses Python identifier FILES
    __FILES = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'FILES'), 'FILES', '__AbsentNamespace0_CTD_ANON__FILES', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.run.xsd', 70, 36), )

    
    FILES = property(__FILES.value, __FILES.set, None, ' Data files associated with the run.')

    
    # Attribute member_name uses Python identifier member_name
    __member_name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'member_name'), 'member_name', '__AbsentNamespace0_CTD_ANON__member_name', pyxb.binding.datatypes.string)
    __member_name._DeclarationLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.run.xsd', 459, 32)
    __member_name._UseLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.run.xsd', 459, 32)
    
    member_name = property(__member_name.value, __member_name.set, None, '\n                                        Allow for an individual DATA_BLOCK to be associated with a member of a sample pool.\n                                    ')

    _ElementMap.update({
        __FILES.name() : __FILES
    })
    _AttributeMap.update({
        __member_name.name() : __member_name
    })
_module_typeBindings.CTD_ANON_ = CTD_ANON_


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """ Data files associated with the run."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.run.xsd', 74, 40)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element FILE uses Python identifier FILE
    __FILE = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'FILE'), 'FILE', '__AbsentNamespace0_CTD_ANON_2_FILE', True, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.run.xsd', 76, 48), )

    
    FILE = property(__FILE.value, __FILE.set, None, None)

    _ElementMap.update({
        __FILE.name() : __FILE
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_2 = CTD_ANON_2


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    """
                            Links to resources related to this RUN or RUN set (publication, datasets, online databases).
                        """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.run.xsd', 475, 24)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element RUN_LINK uses Python identifier RUN_LINK
    __RUN_LINK = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'RUN_LINK'), 'RUN_LINK', '__AbsentNamespace0_CTD_ANON_3_RUN_LINK', True, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.run.xsd', 477, 32), )

    
    RUN_LINK = property(__RUN_LINK.value, __RUN_LINK.set, None, None)

    _ElementMap.update({
        __RUN_LINK.name() : __RUN_LINK
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_3 = CTD_ANON_3


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_4 (pyxb.binding.basis.complexTypeDefinition):
    """
                            Properties and attributes of a RUN.  These can be entered as free-form 
                            tag-value pairs. For certain studies, submitters may be asked to follow a
                            community established ontology when describing the work.
                        """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.run.xsd', 491, 24)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element RUN_ATTRIBUTE uses Python identifier RUN_ATTRIBUTE
    __RUN_ATTRIBUTE = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'RUN_ATTRIBUTE'), 'RUN_ATTRIBUTE', '__AbsentNamespace0_CTD_ANON_4_RUN_ATTRIBUTE', True, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.run.xsd', 493, 32), )

    
    RUN_ATTRIBUTE = property(__RUN_ATTRIBUTE.value, __RUN_ATTRIBUTE.set, None, None)

    _ElementMap.update({
        __RUN_ATTRIBUTE.name() : __RUN_ATTRIBUTE
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_4 = CTD_ANON_4


# Complex type RunSetType with content type ELEMENT_ONLY
class RunSetType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type RunSetType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RunSetType')
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.run.xsd', 518, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element RUN uses Python identifier RUN
    __RUN = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'RUN'), 'RUN', '__AbsentNamespace0_RunSetType_RUN', True, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.run.xsd', 520, 12), )

    
    RUN = property(__RUN.value, __RUN.set, None, None)

    _ElementMap.update({
        __RUN.name() : __RUN
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.RunSetType = RunSetType
Namespace.addCategoryObject('typeBinding', 'RunSetType', RunSetType)


# Complex type RunType with content type ELEMENT_ONLY
class RunType (_ImportedBinding__com.ObjectType):
    """
                A run contains a group of reads generated for a particular experiment.
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RunType')
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.run.xsd', 17, 4)
    _ElementMap = _ImportedBinding__com.ObjectType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__com.ObjectType._AttributeMap.copy()
    # Base type is _ImportedBinding__com.ObjectType
    
    # Element TITLE uses Python identifier TITLE
    __TITLE = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'TITLE'), 'TITLE', '__AbsentNamespace0_RunType_TITLE', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.run.xsd', 26, 20), )

    
    TITLE = property(__TITLE.value, __TITLE.set, None, '\n                        Short text that can be used to define submissions in searches or in displays.\n                   ')

    
    # Element EXPERIMENT_REF uses Python identifier EXPERIMENT_REF
    __EXPERIMENT_REF = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'EXPERIMENT_REF'), 'EXPERIMENT_REF', '__AbsentNamespace0_RunType_EXPERIMENT_REF', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.run.xsd', 33, 20), )

    
    EXPERIMENT_REF = property(__EXPERIMENT_REF.value, __EXPERIMENT_REF.set, None, 'Identifies the parent experiment.\n                   ')

    
    # Element SPOT_DESCRIPTOR uses Python identifier SPOT_DESCRIPTOR
    __SPOT_DESCRIPTOR = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'SPOT_DESCRIPTOR'), 'SPOT_DESCRIPTOR', '__AbsentNamespace0_RunType_SPOT_DESCRIPTOR', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.run.xsd', 45, 20), )

    
    SPOT_DESCRIPTOR = property(__SPOT_DESCRIPTOR.value, __SPOT_DESCRIPTOR.set, None, None)

    
    # Element PLATFORM uses Python identifier PLATFORM
    __PLATFORM = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'PLATFORM'), 'PLATFORM', '__AbsentNamespace0_RunType_PLATFORM', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.run.xsd', 48, 20), )

    
    PLATFORM = property(__PLATFORM.value, __PLATFORM.set, None, None)

    
    # Element PROCESSING uses Python identifier PROCESSING
    __PROCESSING = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'PROCESSING'), 'PROCESSING', '__AbsentNamespace0_RunType_PROCESSING', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.run.xsd', 50, 20), )

    
    PROCESSING = property(__PROCESSING.value, __PROCESSING.set, None, None)

    
    # Element RUN_TYPE uses Python identifier RUN_TYPE
    __RUN_TYPE = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'RUN_TYPE'), 'RUN_TYPE', '__AbsentNamespace0_RunType_RUN_TYPE', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.run.xsd', 53, 20), )

    
    RUN_TYPE = property(__RUN_TYPE.value, __RUN_TYPE.set, None, 'The type of the run. ')

    
    # Element DATA_BLOCK uses Python identifier DATA_BLOCK
    __DATA_BLOCK = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'DATA_BLOCK'), 'DATA_BLOCK', '__AbsentNamespace0_RunType_DATA_BLOCK', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.run.xsd', 66, 24), )

    
    DATA_BLOCK = property(__DATA_BLOCK.value, __DATA_BLOCK.set, None, None)

    
    # Element RUN_LINKS uses Python identifier RUN_LINKS
    __RUN_LINKS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'RUN_LINKS'), 'RUN_LINKS', '__AbsentNamespace0_RunType_RUN_LINKS', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.run.xsd', 469, 20), )

    
    RUN_LINKS = property(__RUN_LINKS.value, __RUN_LINKS.set, None, '\n                            Links to resources related to this RUN or RUN set (publication, datasets, online databases).\n                        ')

    
    # Element RUN_ATTRIBUTES uses Python identifier RUN_ATTRIBUTES
    __RUN_ATTRIBUTES = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'RUN_ATTRIBUTES'), 'RUN_ATTRIBUTES', '__AbsentNamespace0_RunType_RUN_ATTRIBUTES', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.run.xsd', 483, 20), )

    
    RUN_ATTRIBUTES = property(__RUN_ATTRIBUTES.value, __RUN_ATTRIBUTES.set, None, '\n                            Properties and attributes of a RUN.  These can be entered as free-form \n                            tag-value pairs. For certain studies, submitters may be asked to follow a\n                            community established ontology when describing the work.\n                        ')

    
    # Element IDENTIFIERS (IDENTIFIERS) inherited from {SRA.common}ObjectType
    
    # Attribute run_date uses Python identifier run_date
    __run_date = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'run_date'), 'run_date', '__AbsentNamespace0_RunType_run_date', pyxb.binding.datatypes.dateTime)
    __run_date._DeclarationLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.run.xsd', 499, 16)
    __run_date._UseLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.run.xsd', 499, 16)
    
    run_date = property(__run_date.value, __run_date.set, None, '\n                        ISO date when the run took place.  \n                    ')

    
    # Attribute run_center uses Python identifier run_center
    __run_center = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'run_center'), 'run_center', '__AbsentNamespace0_RunType_run_center', pyxb.binding.datatypes.string)
    __run_center._DeclarationLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.run.xsd', 506, 16)
    __run_center._UseLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.run.xsd', 506, 16)
    
    run_center = property(__run_center.value, __run_center.set, None, '\n                        If applicable, the name of the contract sequencing center that executed the run.\n                        Example: 454MSC.\n                    ')

    
    # Attribute alias inherited from {SRA.common}ObjectType
    
    # Attribute center_name inherited from {SRA.common}ObjectType
    
    # Attribute broker_name inherited from {SRA.common}ObjectType
    
    # Attribute accession inherited from {SRA.common}ObjectType
    _ElementMap.update({
        __TITLE.name() : __TITLE,
        __EXPERIMENT_REF.name() : __EXPERIMENT_REF,
        __SPOT_DESCRIPTOR.name() : __SPOT_DESCRIPTOR,
        __PLATFORM.name() : __PLATFORM,
        __PROCESSING.name() : __PROCESSING,
        __RUN_TYPE.name() : __RUN_TYPE,
        __DATA_BLOCK.name() : __DATA_BLOCK,
        __RUN_LINKS.name() : __RUN_LINKS,
        __RUN_ATTRIBUTES.name() : __RUN_ATTRIBUTES
    })
    _AttributeMap.update({
        __run_date.name() : __run_date,
        __run_center.name() : __run_center
    })
_module_typeBindings.RunType = RunType
Namespace.addCategoryObject('typeBinding', 'RunType', RunType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_5 (_ImportedBinding__com.RefObjectType):
    """Identifies the parent experiment.
                   """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.run.xsd', 38, 24)
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
_module_typeBindings.CTD_ANON_5 = CTD_ANON_5


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_6 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.run.xsd', 77, 50)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element READ_LABEL uses Python identifier READ_LABEL
    __READ_LABEL = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'READ_LABEL'), 'READ_LABEL', '__AbsentNamespace0_CTD_ANON_6_READ_LABEL', True, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.run.xsd', 79, 50), )

    
    READ_LABEL = property(__READ_LABEL.value, __READ_LABEL.set, None, '\n                                                        The READ_LABEL can associate a certain file to a certain read_label defined in the SPOT_DESCRIPTOR.\n                                                    ')

    
    # Attribute filename uses Python identifier filename
    __filename = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'filename'), 'filename', '__AbsentNamespace0_CTD_ANON_6_filename', pyxb.binding.datatypes.string, required=True)
    __filename._DeclarationLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.run.xsd', 88, 50)
    __filename._UseLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.run.xsd', 88, 50)
    
    filename = property(__filename.value, __filename.set, None, 'The name or relative pathname of a run data file.')

    
    # Attribute filetype uses Python identifier filetype
    __filetype = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'filetype'), 'filetype', '__AbsentNamespace0_CTD_ANON_6_filetype', _module_typeBindings.STD_ANON, required=True)
    __filetype._DeclarationLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.run.xsd', 94, 50)
    __filetype._UseLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.run.xsd', 94, 50)
    
    filetype = property(__filetype.value, __filetype.set, None, ' The run data file model.')

    
    # Attribute quality_scoring_system uses Python identifier quality_scoring_system
    __quality_scoring_system = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'quality_scoring_system'), 'quality_scoring_system', '__AbsentNamespace0_CTD_ANON_6_quality_scoring_system', _module_typeBindings.STD_ANON_)
    __quality_scoring_system._DeclarationLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.run.xsd', 321, 50)
    __quality_scoring_system._UseLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.run.xsd', 321, 50)
    
    quality_scoring_system = property(__quality_scoring_system.value, __quality_scoring_system.set, None, '\n                                                    How the input data are scored for quality.  \n                                                ')

    
    # Attribute quality_encoding uses Python identifier quality_encoding
    __quality_encoding = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'quality_encoding'), 'quality_encoding', '__AbsentNamespace0_CTD_ANON_6_quality_encoding', _module_typeBindings.STD_ANON_2)
    __quality_encoding._DeclarationLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.run.xsd', 351, 50)
    __quality_encoding._UseLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.run.xsd', 351, 50)
    
    quality_encoding = property(__quality_encoding.value, __quality_encoding.set, None, '\n                                                    Character used in representing the minimum quality value. \n                                                    Helps specify how to decode text rendering of quality data.\n                                                ')

    
    # Attribute ascii_offset uses Python identifier ascii_offset
    __ascii_offset = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ascii_offset'), 'ascii_offset', '__AbsentNamespace0_CTD_ANON_6_ascii_offset', _module_typeBindings.STD_ANON_3)
    __ascii_offset._DeclarationLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.run.xsd', 385, 50)
    __ascii_offset._UseLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.run.xsd', 385, 50)
    
    ascii_offset = property(__ascii_offset.value, __ascii_offset.set, None, '\n                                                    Character used in representing the minimum quality value.  Helps specify how to decode text rendering of quality data.\n                                                ')

    
    # Attribute checksum_method uses Python identifier checksum_method
    __checksum_method = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'checksum_method'), 'checksum_method', '__AbsentNamespace0_CTD_ANON_6_checksum_method', _module_typeBindings.STD_ANON_4, required=True)
    __checksum_method._DeclarationLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.run.xsd', 411, 50)
    __checksum_method._UseLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.run.xsd', 411, 50)
    
    checksum_method = property(__checksum_method.value, __checksum_method.set, None, '\n                                                    Checksum method used.\n                                                ')

    
    # Attribute checksum uses Python identifier checksum
    __checksum = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'checksum'), 'checksum', '__AbsentNamespace0_CTD_ANON_6_checksum', pyxb.binding.datatypes.string, required=True)
    __checksum._DeclarationLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.run.xsd', 437, 50)
    __checksum._UseLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.run.xsd', 437, 50)
    
    checksum = property(__checksum.value, __checksum.set, None, '\n                                                    Checksum of uncompressed file.\n                                                ')

    
    # Attribute unencrypted_checksum uses Python identifier unencrypted_checksum
    __unencrypted_checksum = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'unencrypted_checksum'), 'unencrypted_checksum', '__AbsentNamespace0_CTD_ANON_6_unencrypted_checksum', pyxb.binding.datatypes.string)
    __unencrypted_checksum._DeclarationLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.run.xsd', 445, 50)
    __unencrypted_checksum._UseLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.run.xsd', 445, 50)
    
    unencrypted_checksum = property(__unencrypted_checksum.value, __unencrypted_checksum.set, None, '\n                                                            Checksum of unenrypted file(used in conjunction with checksum of encrypted file).\n                                                        ')

    _ElementMap.update({
        __READ_LABEL.name() : __READ_LABEL
    })
    _AttributeMap.update({
        __filename.name() : __filename,
        __filetype.name() : __filetype,
        __quality_scoring_system.name() : __quality_scoring_system,
        __quality_encoding.name() : __quality_encoding,
        __ascii_offset.name() : __ascii_offset,
        __checksum_method.name() : __checksum_method,
        __checksum.name() : __checksum,
        __unencrypted_checksum.name() : __unencrypted_checksum
    })
_module_typeBindings.CTD_ANON_6 = CTD_ANON_6


RUN_SET = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RUN_SET'), RunSetType, documentation='\n                RUN_SET serves as a container for a set of runs and a name space\n                for establishing referential integrity between them. \n            ', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.run.xsd', 524, 4))
Namespace.addCategoryObject('elementBinding', RUN_SET.name().localName(), RUN_SET)

RUN = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RUN'), RunType, location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.run.xsd', 534, 4))
Namespace.addCategoryObject('elementBinding', RUN.name().localName(), RUN)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'REFERENCE_ALIGNMENT'), _ImportedBinding__com.ReferenceSequenceType, scope=CTD_ANON, location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.run.xsd', 59, 32)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'REFERENCE_ALIGNMENT')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.run.xsd', 59, 32))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'FILES'), CTD_ANON_2, scope=CTD_ANON_, documentation=' Data files associated with the run.', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.run.xsd', 70, 36)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, 'FILES')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.run.xsd', 70, 36))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_()




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'FILE'), CTD_ANON_6, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.run.xsd', 76, 48)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(None, 'FILE')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.run.xsd', 76, 48))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_2._Automaton = _BuildAutomaton_2()




CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'RUN_LINK'), _ImportedBinding__com.LinkType, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.run.xsd', 477, 32)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(None, 'RUN_LINK')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.run.xsd', 477, 32))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_3._Automaton = _BuildAutomaton_3()




CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'RUN_ATTRIBUTE'), _ImportedBinding__com.AttributeType, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.run.xsd', 493, 32)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(None, 'RUN_ATTRIBUTE')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.run.xsd', 493, 32))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_4._Automaton = _BuildAutomaton_4()




RunSetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'RUN'), RunType, scope=RunSetType, location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.run.xsd', 520, 12)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(RunSetType._UseForTag(pyxb.namespace.ExpandedName(None, 'RUN')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.run.xsd', 520, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
RunSetType._Automaton = _BuildAutomaton_5()




RunType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'TITLE'), pyxb.binding.datatypes.string, scope=RunType, documentation='\n                        Short text that can be used to define submissions in searches or in displays.\n                   ', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.run.xsd', 26, 20)))

RunType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'EXPERIMENT_REF'), CTD_ANON_5, scope=RunType, documentation='Identifies the parent experiment.\n                   ', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.run.xsd', 33, 20)))

RunType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'SPOT_DESCRIPTOR'), _ImportedBinding__com.SpotDescriptorType, scope=RunType, location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.run.xsd', 45, 20)))

RunType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'PLATFORM'), _ImportedBinding__com.PlatformType, scope=RunType, location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.run.xsd', 48, 20)))

RunType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'PROCESSING'), _ImportedBinding__com.ProcessingType, scope=RunType, location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.run.xsd', 50, 20)))

RunType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'RUN_TYPE'), CTD_ANON, scope=RunType, documentation='The type of the run. ', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.run.xsd', 53, 20)))

RunType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'DATA_BLOCK'), CTD_ANON_, scope=RunType, location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.run.xsd', 66, 24)))

RunType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'RUN_LINKS'), CTD_ANON_3, scope=RunType, documentation='\n                            Links to resources related to this RUN or RUN set (publication, datasets, online databases).\n                        ', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.run.xsd', 469, 20)))

RunType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'RUN_ATTRIBUTES'), CTD_ANON_4, scope=RunType, documentation='\n                            Properties and attributes of a RUN.  These can be entered as free-form \n                            tag-value pairs. For certain studies, submitters may be asked to follow a\n                            community established ontology when describing the work.\n                        ', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.run.xsd', 483, 20)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 19, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.run.xsd', 26, 20))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.run.xsd', 45, 20))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.run.xsd', 48, 20))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.run.xsd', 50, 20))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.run.xsd', 53, 20))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.run.xsd', 66, 24))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.run.xsd', 469, 20))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.run.xsd', 483, 20))
    counters.add(cc_8)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RunType._UseForTag(pyxb.namespace.ExpandedName(None, 'IDENTIFIERS')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 19, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RunType._UseForTag(pyxb.namespace.ExpandedName(None, 'TITLE')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.run.xsd', 26, 20))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(RunType._UseForTag(pyxb.namespace.ExpandedName(None, 'EXPERIMENT_REF')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.run.xsd', 33, 20))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(RunType._UseForTag(pyxb.namespace.ExpandedName(None, 'SPOT_DESCRIPTOR')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.run.xsd', 45, 20))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(RunType._UseForTag(pyxb.namespace.ExpandedName(None, 'PLATFORM')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.run.xsd', 48, 20))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(RunType._UseForTag(pyxb.namespace.ExpandedName(None, 'PROCESSING')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.run.xsd', 50, 20))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(RunType._UseForTag(pyxb.namespace.ExpandedName(None, 'RUN_TYPE')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.run.xsd', 53, 20))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(RunType._UseForTag(pyxb.namespace.ExpandedName(None, 'DATA_BLOCK')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.run.xsd', 66, 24))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(RunType._UseForTag(pyxb.namespace.ExpandedName(None, 'RUN_LINKS')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.run.xsd', 469, 20))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(RunType._UseForTag(pyxb.namespace.ExpandedName(None, 'RUN_ATTRIBUTES')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.run.xsd', 483, 20))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
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
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, True) ]))
    st_9._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
RunType._Automaton = _BuildAutomaton_6()




def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 53, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(None, 'IDENTIFIERS')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 53, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_5._Automaton = _BuildAutomaton_7()




CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'READ_LABEL'), pyxb.binding.datatypes.string, scope=CTD_ANON_6, documentation='\n                                                        The READ_LABEL can associate a certain file to a certain read_label defined in the SPOT_DESCRIPTOR.\n                                                    ', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.run.xsd', 79, 50)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.run.xsd', 79, 50))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(None, 'READ_LABEL')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.run.xsd', 79, 50))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_6._Automaton = _BuildAutomaton_8()

