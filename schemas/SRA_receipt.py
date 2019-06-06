# ./SRA_receipt.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2019-06-06 19:25:13.649706 by PyXB version 1.2.6 using Python 3.6.7.final.0
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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:0ad5ddc6-8880-11e9-9350-b0c090509cda')

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
class STD_ANON (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.receipt.xsd', 24, 24)
    _Documentation = None
STD_ANON._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(1024))
STD_ANON._InitializeFacetMap(STD_ANON._CF_minLength,
   STD_ANON._CF_maxLength)
_module_typeBindings.STD_ANON = STD_ANON

# Atomic simple type: [anonymous]
class STD_ANON_ (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.receipt.xsd', 32, 24)
    _Documentation = None
STD_ANON_._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_, enum_prefix=None)
STD_ANON_.study = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='study', tag='study')
STD_ANON_.experiment = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='experiment', tag='experiment')
STD_ANON_.sample = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='sample', tag='sample')
STD_ANON_.sampleGroup = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='sampleGroup', tag='sampleGroup')
STD_ANON_.run = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='run', tag='run')
STD_ANON_.analysis = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='analysis', tag='analysis')
STD_ANON_.dataset = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='dataset', tag='dataset')
STD_ANON_.policy = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='policy', tag='policy')
STD_ANON_.dac = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='dac', tag='dac')
STD_ANON_.ArrayExpress = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='ArrayExpress', tag='ArrayExpress')
STD_ANON_.LocusTagPrefix = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='LocusTagPrefix', tag='LocusTagPrefix')
STD_ANON_.Taxon = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='Taxon', tag='Taxon')
STD_ANON_.Project = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='Project', tag='Project')
STD_ANON_.checklist = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='checklist', tag='checklist')
STD_ANON_.biosample = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='biosample', tag='biosample')
STD_ANON_._InitializeFacetMap(STD_ANON_._CF_enumeration)
_module_typeBindings.STD_ANON_ = STD_ANON_

# Atomic simple type: [anonymous]
class STD_ANON_2 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.receipt.xsd', 59, 12)
    _Documentation = None
STD_ANON_2._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_2, enum_prefix=None)
STD_ANON_2.PRIVATE = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='PRIVATE', tag='PRIVATE')
STD_ANON_2.PUBLIC = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='PUBLIC', tag='PUBLIC')
STD_ANON_2.KILLED = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='KILLED', tag='KILLED')
STD_ANON_2.SUPPRESSED = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='SUPPRESSED', tag='SUPPRESSED')
STD_ANON_2._InitializeFacetMap(STD_ANON_2._CF_enumeration)
_module_typeBindings.STD_ANON_2 = STD_ANON_2

# Atomic simple type: [anonymous]
class STD_ANON_3 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.receipt.xsd', 95, 20)
    _Documentation = None
STD_ANON_3._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_3, enum_prefix=None)
STD_ANON_3.ADD = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='ADD', tag='ADD')
STD_ANON_3.MODIFY = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='MODIFY', tag='MODIFY')
STD_ANON_3.RELEASE = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='RELEASE', tag='RELEASE')
STD_ANON_3.HOLD = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='HOLD', tag='HOLD')
STD_ANON_3.VALIDATE = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='VALIDATE', tag='VALIDATE')
STD_ANON_3.PROTECT = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='PROTECT', tag='PROTECT')
STD_ANON_3.RECEIPT = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='RECEIPT', tag='RECEIPT')
STD_ANON_3.ROLLBACK = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='ROLLBACK', tag='ROLLBACK')
STD_ANON_3._InitializeFacetMap(STD_ANON_3._CF_enumeration)
_module_typeBindings.STD_ANON_3 = STD_ANON_3

# Atomic simple type: [anonymous]
class STD_ANON_4 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.receipt.xsd', 112, 16)
    _Documentation = None
STD_ANON_4._CF_pattern = pyxb.binding.facets.CF_pattern()
STD_ANON_4._CF_pattern.addPattern(pattern='.+\\.xml')
STD_ANON_4._InitializeFacetMap(STD_ANON_4._CF_pattern)
_module_typeBindings.STD_ANON_4 = STD_ANON_4

# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.receipt.xsd', 85, 20)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element ERROR uses Python identifier ERROR
    __ERROR = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ERROR'), 'ERROR', '__AbsentNamespace0_CTD_ANON_ERROR', True, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.receipt.xsd', 87, 28), )

    
    ERROR = property(__ERROR.value, __ERROR.set, None, None)

    
    # Element INFO uses Python identifier INFO
    __INFO = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'INFO'), 'INFO', '__AbsentNamespace0_CTD_ANON_INFO', True, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.receipt.xsd', 89, 28), )

    
    INFO = property(__INFO.value, __INFO.set, None, None)

    _ElementMap.update({
        __ERROR.name() : __ERROR,
        __INFO.name() : __INFO
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON = CTD_ANON


# Complex type ID with content type ELEMENT_ONLY
class ID (pyxb.binding.basis.complexTypeDefinition):
    """Complex type ID with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ID')
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.receipt.xsd', 15, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element EXT_ID uses Python identifier EXT_ID
    __EXT_ID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'EXT_ID'), 'EXT_ID', '__AbsentNamespace0_ID_EXT_ID', True, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.receipt.xsd', 17, 12), )

    
    EXT_ID = property(__EXT_ID.value, __EXT_ID.set, None, 'The REF identifies the reference of that object .\n                    ')

    
    # Attribute accession uses Python identifier accession
    __accession = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'accession'), 'accession', '__AbsentNamespace0_ID_accession', pyxb.binding.datatypes.string)
    __accession._DeclarationLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.receipt.xsd', 55, 8)
    __accession._UseLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.receipt.xsd', 55, 8)
    
    accession = property(__accession.value, __accession.set, None, None)

    
    # Attribute alias uses Python identifier alias
    __alias = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'alias'), 'alias', '__AbsentNamespace0_ID_alias', pyxb.binding.datatypes.string, required=True)
    __alias._DeclarationLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.receipt.xsd', 56, 8)
    __alias._UseLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.receipt.xsd', 56, 8)
    
    alias = property(__alias.value, __alias.set, None, None)

    
    # Attribute holdUntilDate uses Python identifier holdUntilDate
    __holdUntilDate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'holdUntilDate'), 'holdUntilDate', '__AbsentNamespace0_ID_holdUntilDate', pyxb.binding.datatypes.date)
    __holdUntilDate._DeclarationLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.receipt.xsd', 57, 8)
    __holdUntilDate._UseLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.receipt.xsd', 57, 8)
    
    holdUntilDate = property(__holdUntilDate.value, __holdUntilDate.set, None, None)

    
    # Attribute status uses Python identifier status
    __status = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'status'), 'status', '__AbsentNamespace0_ID_status', _module_typeBindings.STD_ANON_2)
    __status._DeclarationLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.receipt.xsd', 58, 8)
    __status._UseLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.receipt.xsd', 58, 8)
    
    status = property(__status.value, __status.set, None, None)

    _ElementMap.update({
        __EXT_ID.name() : __EXT_ID
    })
    _AttributeMap.update({
        __accession.name() : __accession,
        __alias.name() : __alias,
        __holdUntilDate.name() : __holdUntilDate,
        __status.name() : __status
    })
_module_typeBindings.ID = ID
Namespace.addCategoryObject('typeBinding', 'ID', ID)


# Complex type [anonymous] with content type EMPTY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """The REF identifies the reference of that object .
                    """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.receipt.xsd', 22, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute accession uses Python identifier accession
    __accession = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'accession'), 'accession', '__AbsentNamespace0_CTD_ANON__accession', _module_typeBindings.STD_ANON)
    __accession._DeclarationLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.receipt.xsd', 23, 20)
    __accession._UseLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.receipt.xsd', 23, 20)
    
    accession = property(__accession.value, __accession.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__AbsentNamespace0_CTD_ANON__type', _module_typeBindings.STD_ANON_)
    __type._DeclarationLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.receipt.xsd', 31, 20)
    __type._UseLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.receipt.xsd', 31, 20)
    
    type = property(__type.value, __type.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __accession.name() : __accession,
        __type.name() : __type
    })
_module_typeBindings.CTD_ANON_ = CTD_ANON_


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.receipt.xsd', 70, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element ANALYSIS uses Python identifier ANALYSIS
    __ANALYSIS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ANALYSIS'), 'ANALYSIS', '__AbsentNamespace0_CTD_ANON_2_ANALYSIS', True, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.receipt.xsd', 72, 16), )

    
    ANALYSIS = property(__ANALYSIS.value, __ANALYSIS.set, None, None)

    
    # Element EXPERIMENT uses Python identifier EXPERIMENT
    __EXPERIMENT = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'EXPERIMENT'), 'EXPERIMENT', '__AbsentNamespace0_CTD_ANON_2_EXPERIMENT', True, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.receipt.xsd', 73, 16), )

    
    EXPERIMENT = property(__EXPERIMENT.value, __EXPERIMENT.set, None, None)

    
    # Element RUN uses Python identifier RUN
    __RUN = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'RUN'), 'RUN', '__AbsentNamespace0_CTD_ANON_2_RUN', True, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.receipt.xsd', 74, 16), )

    
    RUN = property(__RUN.value, __RUN.set, None, None)

    
    # Element SAMPLE uses Python identifier SAMPLE
    __SAMPLE = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'SAMPLE'), 'SAMPLE', '__AbsentNamespace0_CTD_ANON_2_SAMPLE', True, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.receipt.xsd', 75, 16), )

    
    SAMPLE = property(__SAMPLE.value, __SAMPLE.set, None, None)

    
    # Element SAMPLEGROUP uses Python identifier SAMPLEGROUP
    __SAMPLEGROUP = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'SAMPLEGROUP'), 'SAMPLEGROUP', '__AbsentNamespace0_CTD_ANON_2_SAMPLEGROUP', True, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.receipt.xsd', 76, 16), )

    
    SAMPLEGROUP = property(__SAMPLEGROUP.value, __SAMPLEGROUP.set, None, None)

    
    # Element STUDY uses Python identifier STUDY
    __STUDY = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'STUDY'), 'STUDY', '__AbsentNamespace0_CTD_ANON_2_STUDY', True, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.receipt.xsd', 77, 16), )

    
    STUDY = property(__STUDY.value, __STUDY.set, None, None)

    
    # Element DAC uses Python identifier DAC
    __DAC = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'DAC'), 'DAC', '__AbsentNamespace0_CTD_ANON_2_DAC', True, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.receipt.xsd', 78, 16), )

    
    DAC = property(__DAC.value, __DAC.set, None, None)

    
    # Element POLICY uses Python identifier POLICY
    __POLICY = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'POLICY'), 'POLICY', '__AbsentNamespace0_CTD_ANON_2_POLICY', True, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.receipt.xsd', 79, 16), )

    
    POLICY = property(__POLICY.value, __POLICY.set, None, None)

    
    # Element DATASET uses Python identifier DATASET
    __DATASET = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'DATASET'), 'DATASET', '__AbsentNamespace0_CTD_ANON_2_DATASET', True, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.receipt.xsd', 80, 16), )

    
    DATASET = property(__DATASET.value, __DATASET.set, None, None)

    
    # Element PROJECT uses Python identifier PROJECT
    __PROJECT = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'PROJECT'), 'PROJECT', '__AbsentNamespace0_CTD_ANON_2_PROJECT', True, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.receipt.xsd', 81, 16), )

    
    PROJECT = property(__PROJECT.value, __PROJECT.set, None, None)

    
    # Element CHECKLIST uses Python identifier CHECKLIST
    __CHECKLIST = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'CHECKLIST'), 'CHECKLIST', '__AbsentNamespace0_CTD_ANON_2_CHECKLIST', True, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.receipt.xsd', 82, 16), )

    
    CHECKLIST = property(__CHECKLIST.value, __CHECKLIST.set, None, None)

    
    # Element SUBMISSION uses Python identifier SUBMISSION
    __SUBMISSION = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'SUBMISSION'), 'SUBMISSION', '__AbsentNamespace0_CTD_ANON_2_SUBMISSION', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.receipt.xsd', 83, 16), )

    
    SUBMISSION = property(__SUBMISSION.value, __SUBMISSION.set, None, None)

    
    # Element MESSAGES uses Python identifier MESSAGES
    __MESSAGES = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'MESSAGES'), 'MESSAGES', '__AbsentNamespace0_CTD_ANON_2_MESSAGES', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.receipt.xsd', 84, 16), )

    
    MESSAGES = property(__MESSAGES.value, __MESSAGES.set, None, None)

    
    # Element ACTIONS uses Python identifier ACTIONS
    __ACTIONS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ACTIONS'), 'ACTIONS', '__AbsentNamespace0_CTD_ANON_2_ACTIONS', True, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.receipt.xsd', 94, 16), )

    
    ACTIONS = property(__ACTIONS.value, __ACTIONS.set, None, None)

    
    # Attribute success uses Python identifier success
    __success = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'success'), 'success', '__AbsentNamespace0_CTD_ANON_2_success', pyxb.binding.datatypes.boolean, required=True)
    __success._DeclarationLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.receipt.xsd', 109, 12)
    __success._UseLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.receipt.xsd', 109, 12)
    
    success = property(__success.value, __success.set, None, None)

    
    # Attribute receiptDate uses Python identifier receiptDate
    __receiptDate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'receiptDate'), 'receiptDate', '__AbsentNamespace0_CTD_ANON_2_receiptDate', pyxb.binding.datatypes.dateTime, required=True)
    __receiptDate._DeclarationLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.receipt.xsd', 110, 12)
    __receiptDate._UseLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.receipt.xsd', 110, 12)
    
    receiptDate = property(__receiptDate.value, __receiptDate.set, None, None)

    
    # Attribute submissionFile uses Python identifier submissionFile
    __submissionFile = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'submissionFile'), 'submissionFile', '__AbsentNamespace0_CTD_ANON_2_submissionFile', _module_typeBindings.STD_ANON_4, required=True)
    __submissionFile._DeclarationLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.receipt.xsd', 111, 12)
    __submissionFile._UseLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.receipt.xsd', 111, 12)
    
    submissionFile = property(__submissionFile.value, __submissionFile.set, None, None)

    _ElementMap.update({
        __ANALYSIS.name() : __ANALYSIS,
        __EXPERIMENT.name() : __EXPERIMENT,
        __RUN.name() : __RUN,
        __SAMPLE.name() : __SAMPLE,
        __SAMPLEGROUP.name() : __SAMPLEGROUP,
        __STUDY.name() : __STUDY,
        __DAC.name() : __DAC,
        __POLICY.name() : __POLICY,
        __DATASET.name() : __DATASET,
        __PROJECT.name() : __PROJECT,
        __CHECKLIST.name() : __CHECKLIST,
        __SUBMISSION.name() : __SUBMISSION,
        __MESSAGES.name() : __MESSAGES,
        __ACTIONS.name() : __ACTIONS
    })
    _AttributeMap.update({
        __success.name() : __success,
        __receiptDate.name() : __receiptDate,
        __submissionFile.name() : __submissionFile
    })
_module_typeBindings.CTD_ANON_2 = CTD_ANON_2


RECEIPT = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RECEIPT'), CTD_ANON_2, location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.receipt.xsd', 69, 4))
Namespace.addCategoryObject('elementBinding', RECEIPT.name().localName(), RECEIPT)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ERROR'), pyxb.binding.datatypes.string, scope=CTD_ANON, location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.receipt.xsd', 87, 28)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'INFO'), pyxb.binding.datatypes.string, scope=CTD_ANON, location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.receipt.xsd', 89, 28)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.receipt.xsd', 87, 28))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.receipt.xsd', 89, 28))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'ERROR')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.receipt.xsd', 87, 28))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'INFO')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.receipt.xsd', 89, 28))
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
CTD_ANON._Automaton = _BuildAutomaton()




ID._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'EXT_ID'), CTD_ANON_, nillable=pyxb.binding.datatypes.boolean(1), scope=ID, documentation='The REF identifies the reference of that object .\n                    ', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.receipt.xsd', 17, 12)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.receipt.xsd', 17, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ID._UseForTag(pyxb.namespace.ExpandedName(None, 'EXT_ID')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.receipt.xsd', 17, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ID._Automaton = _BuildAutomaton_()




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ANALYSIS'), ID, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.receipt.xsd', 72, 16)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'EXPERIMENT'), ID, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.receipt.xsd', 73, 16)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'RUN'), ID, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.receipt.xsd', 74, 16)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'SAMPLE'), ID, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.receipt.xsd', 75, 16)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'SAMPLEGROUP'), ID, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.receipt.xsd', 76, 16)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'STUDY'), ID, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.receipt.xsd', 77, 16)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'DAC'), ID, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.receipt.xsd', 78, 16)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'POLICY'), ID, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.receipt.xsd', 79, 16)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'DATASET'), ID, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.receipt.xsd', 80, 16)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'PROJECT'), ID, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.receipt.xsd', 81, 16)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'CHECKLIST'), ID, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.receipt.xsd', 82, 16)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'SUBMISSION'), ID, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.receipt.xsd', 83, 16)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'MESSAGES'), CTD_ANON, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.receipt.xsd', 84, 16)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ACTIONS'), STD_ANON_3, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.receipt.xsd', 94, 16)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.receipt.xsd', 72, 16))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.receipt.xsd', 73, 16))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.receipt.xsd', 74, 16))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.receipt.xsd', 75, 16))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.receipt.xsd', 76, 16))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.receipt.xsd', 77, 16))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.receipt.xsd', 78, 16))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.receipt.xsd', 79, 16))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.receipt.xsd', 80, 16))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.receipt.xsd', 81, 16))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.receipt.xsd', 82, 16))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.receipt.xsd', 83, 16))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.receipt.xsd', 84, 16))
    counters.add(cc_12)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(None, 'ANALYSIS')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.receipt.xsd', 72, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(None, 'EXPERIMENT')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.receipt.xsd', 73, 16))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(None, 'RUN')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.receipt.xsd', 74, 16))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(None, 'SAMPLE')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.receipt.xsd', 75, 16))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(None, 'SAMPLEGROUP')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.receipt.xsd', 76, 16))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(None, 'STUDY')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.receipt.xsd', 77, 16))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(None, 'DAC')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.receipt.xsd', 78, 16))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(None, 'POLICY')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.receipt.xsd', 79, 16))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(None, 'DATASET')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.receipt.xsd', 80, 16))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(None, 'PROJECT')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.receipt.xsd', 81, 16))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(None, 'CHECKLIST')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.receipt.xsd', 82, 16))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(None, 'SUBMISSION')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.receipt.xsd', 83, 16))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(None, 'MESSAGES')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.receipt.xsd', 84, 16))
    st_12 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(None, 'ACTIONS')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.receipt.xsd', 94, 16))
    st_13 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
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
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_13, [
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
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
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
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
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
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
         ]))
    st_13._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_2._Automaton = _BuildAutomaton_2()

