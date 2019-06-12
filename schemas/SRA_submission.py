# ./SRA_submission.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2019-06-06 19:25:21.342559 by PyXB version 1.2.6 using Python 3.6.7.final.0
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
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 88, 28)
    _Documentation = None
STD_ANON._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON, enum_prefix=None)
STD_ANON.study = STD_ANON._CF_enumeration.addEnumeration(unicode_value='study', tag='study')
STD_ANON.experiment = STD_ANON._CF_enumeration.addEnumeration(unicode_value='experiment', tag='experiment')
STD_ANON.sample = STD_ANON._CF_enumeration.addEnumeration(unicode_value='sample', tag='sample')
STD_ANON.run = STD_ANON._CF_enumeration.addEnumeration(unicode_value='run', tag='run')
STD_ANON.analysis = STD_ANON._CF_enumeration.addEnumeration(unicode_value='analysis', tag='analysis')
STD_ANON.dataset = STD_ANON._CF_enumeration.addEnumeration(unicode_value='dataset', tag='dataset')
STD_ANON.policy = STD_ANON._CF_enumeration.addEnumeration(unicode_value='policy', tag='policy')
STD_ANON.dac = STD_ANON._CF_enumeration.addEnumeration(unicode_value='dac', tag='dac')
STD_ANON.project = STD_ANON._CF_enumeration.addEnumeration(unicode_value='project', tag='project')
STD_ANON.checklist = STD_ANON._CF_enumeration.addEnumeration(unicode_value='checklist', tag='checklist')
STD_ANON.sampleGroup = STD_ANON._CF_enumeration.addEnumeration(unicode_value='sampleGroup', tag='sampleGroup')
STD_ANON._InitializeFacetMap(STD_ANON._CF_enumeration)
_module_typeBindings.STD_ANON = STD_ANON

# Atomic simple type: [anonymous]
class STD_ANON_ (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 120, 28)
    _Documentation = None
STD_ANON_._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_, enum_prefix=None)
STD_ANON_.study = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='study', tag='study')
STD_ANON_.experiment = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='experiment', tag='experiment')
STD_ANON_.sample = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='sample', tag='sample')
STD_ANON_.run = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='run', tag='run')
STD_ANON_.analysis = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='analysis', tag='analysis')
STD_ANON_.dataset = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='dataset', tag='dataset')
STD_ANON_.policy = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='policy', tag='policy')
STD_ANON_.dac = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='dac', tag='dac')
STD_ANON_.project = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='project', tag='project')
STD_ANON_.checklist = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='checklist', tag='checklist')
STD_ANON_.sampleGroup = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='sampleGroup', tag='sampleGroup')
STD_ANON_._InitializeFacetMap(STD_ANON_._CF_enumeration)
_module_typeBindings.STD_ANON_ = STD_ANON_

# Atomic simple type: [anonymous]
class STD_ANON_2 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 247, 28)
    _Documentation = None
STD_ANON_2._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_2, enum_prefix=None)
STD_ANON_2.study = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='study', tag='study')
STD_ANON_2.experiment = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='experiment', tag='experiment')
STD_ANON_2.sample = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='sample', tag='sample')
STD_ANON_2.run = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='run', tag='run')
STD_ANON_2.analysis = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='analysis', tag='analysis')
STD_ANON_2.dataset = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='dataset', tag='dataset')
STD_ANON_2.policy = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='policy', tag='policy')
STD_ANON_2.dac = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='dac', tag='dac')
STD_ANON_2.project = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='project', tag='project')
STD_ANON_2.checklist = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='checklist', tag='checklist')
STD_ANON_2.sampleGroup = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='sampleGroup', tag='sampleGroup')
STD_ANON_2._InitializeFacetMap(STD_ANON_2._CF_enumeration)
_module_typeBindings.STD_ANON_2 = STD_ANON_2

# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 34, 12)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element CONTACT uses Python identifier CONTACT
    __CONTACT = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'CONTACT'), 'CONTACT', '__AbsentNamespace0_CTD_ANON_CONTACT', True, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 36, 16), )

    
    CONTACT = property(__CONTACT.value, __CONTACT.set, None, None)

    _ElementMap.update({
        __CONTACT.name() : __CONTACT
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON = CTD_ANON


# Complex type [anonymous] with content type EMPTY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 37, 18)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_CTD_ANON__name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 38, 20)
    __name._UseLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 38, 20)
    
    name = property(__name.value, __name.set, None, '\n                      Name of contact person for this submission.\n                    ')

    
    # Attribute inform_on_status uses Python identifier inform_on_status
    __inform_on_status = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'inform_on_status'), 'inform_on_status', '__AbsentNamespace0_CTD_ANON__inform_on_status', pyxb.binding.datatypes.anyURI)
    __inform_on_status._DeclarationLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 45, 20)
    __inform_on_status._UseLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 45, 20)
    
    inform_on_status = property(__inform_on_status.value, __inform_on_status.set, None, '\n                      Internet address of person or service to inform on any status changes for this submission.\n                    ')

    
    # Attribute inform_on_error uses Python identifier inform_on_error
    __inform_on_error = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'inform_on_error'), 'inform_on_error', '__AbsentNamespace0_CTD_ANON__inform_on_error', pyxb.binding.datatypes.anyURI)
    __inform_on_error._DeclarationLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 52, 20)
    __inform_on_error._UseLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 52, 20)
    
    inform_on_error = property(__inform_on_error.value, __inform_on_error.set, None, '\n                      Internet address of person or service to inform on any errors for this submission.\n                    ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __name.name() : __name,
        __inform_on_status.name() : __inform_on_status,
        __inform_on_error.name() : __inform_on_error
    })
_module_typeBindings.CTD_ANON_ = CTD_ANON_


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 66, 12)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element ACTION uses Python identifier ACTION
    __ACTION = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ACTION'), 'ACTION', '__AbsentNamespace0_CTD_ANON_2_ACTION', True, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 68, 16), )

    
    ACTION = property(__ACTION.value, __ACTION.set, None, 'Action to be executed by the archive.')

    _ElementMap.update({
        __ACTION.name() : __ACTION
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_2 = CTD_ANON_2


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    """Action to be executed by the archive."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 72, 18)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element ADD uses Python identifier ADD
    __ADD = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ADD'), 'ADD', '__AbsentNamespace0_CTD_ANON_3_ADD', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 74, 22), )

    
    ADD = property(__ADD.value, __ADD.set, None, 'Add an object to the archive.')

    
    # Element MODIFY uses Python identifier MODIFY
    __MODIFY = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'MODIFY'), 'MODIFY', '__AbsentNamespace0_CTD_ANON_3_MODIFY', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 106, 22), )

    
    MODIFY = property(__MODIFY.value, __MODIFY.set, None, 'Modify an object in the archive.')

    
    # Element CANCEL uses Python identifier CANCEL
    __CANCEL = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'CANCEL'), 'CANCEL', '__AbsentNamespace0_CTD_ANON_3_CANCEL', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 138, 22), )

    
    CANCEL = property(__CANCEL.value, __CANCEL.set, None, 'Cancels a private object and its dependent objects.')

    
    # Element SUPPRESS uses Python identifier SUPPRESS
    __SUPPRESS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'SUPPRESS'), 'SUPPRESS', '__AbsentNamespace0_CTD_ANON_3_SUPPRESS', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 150, 22), )

    
    SUPPRESS = property(__SUPPRESS.value, __SUPPRESS.set, None, 'Suppresses a public object and its dependent objects.')

    
    # Element KILL uses Python identifier KILL
    __KILL = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'KILL'), 'KILL', '__AbsentNamespace0_CTD_ANON_3_KILL', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 167, 22), )

    
    KILL = property(__KILL.value, __KILL.set, None, 'Kills a public object and its dependent objects.')

    
    # Element HOLD uses Python identifier HOLD
    __HOLD = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'HOLD'), 'HOLD', '__AbsentNamespace0_CTD_ANON_3_HOLD', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 184, 22), )

    
    HOLD = property(__HOLD.value, __HOLD.set, None, 'Make the object public only when the hold date expires.')

    
    # Element RELEASE uses Python identifier RELEASE
    __RELEASE = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'RELEASE'), 'RELEASE', '__AbsentNamespace0_CTD_ANON_3_RELEASE', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 205, 22), )

    
    RELEASE = property(__RELEASE.value, __RELEASE.set, None, 'The object will be released immediately to public.')

    
    # Element PROTECT uses Python identifier PROTECT
    __PROTECT = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'PROTECT'), 'PROTECT', '__AbsentNamespace0_CTD_ANON_3_PROTECT', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 221, 22), )

    
    PROTECT = property(__PROTECT.value, __PROTECT.set, None, 'This action is required for data submitted to European Genome-Phenome Archive (EGA). ')

    
    # Element ROLLBACK uses Python identifier ROLLBACK
    __ROLLBACK = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ROLLBACK'), 'ROLLBACK', '__AbsentNamespace0_CTD_ANON_3_ROLLBACK', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 227, 22), )

    
    ROLLBACK = property(__ROLLBACK.value, __ROLLBACK.set, None, 'This action will rollback the submission from the database')

    
    # Element VALIDATE uses Python identifier VALIDATE
    __VALIDATE = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'VALIDATE'), 'VALIDATE', '__AbsentNamespace0_CTD_ANON_3_VALIDATE', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 233, 22), )

    
    VALIDATE = property(__VALIDATE.value, __VALIDATE.set, None, 'Validates the submitted XMLs without actually submitting them.')

    
    # Element RECEIPT uses Python identifier RECEIPT
    __RECEIPT = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'RECEIPT'), 'RECEIPT', '__AbsentNamespace0_CTD_ANON_3_RECEIPT', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 265, 22), )

    
    RECEIPT = property(__RECEIPT.value, __RECEIPT.set, None, 'Returns the receipt for a given submission alias.')

    _ElementMap.update({
        __ADD.name() : __ADD,
        __MODIFY.name() : __MODIFY,
        __CANCEL.name() : __CANCEL,
        __SUPPRESS.name() : __SUPPRESS,
        __KILL.name() : __KILL,
        __HOLD.name() : __HOLD,
        __RELEASE.name() : __RELEASE,
        __PROTECT.name() : __PROTECT,
        __ROLLBACK.name() : __ROLLBACK,
        __VALIDATE.name() : __VALIDATE,
        __RECEIPT.name() : __RECEIPT
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_3 = CTD_ANON_3


# Complex type [anonymous] with content type EMPTY
class CTD_ANON_4 (pyxb.binding.basis.complexTypeDefinition):
    """Cancels a private object and its dependent objects."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 142, 24)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute target uses Python identifier target
    __target = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'target'), 'target', '__AbsentNamespace0_CTD_ANON_4_target', pyxb.binding.datatypes.string, required=True)
    __target._DeclarationLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 143, 26)
    __target._UseLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 143, 26)
    
    target = property(__target.value, __target.set, None, 'Accession or refname of the object that is being cancelled.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __target.name() : __target
    })
_module_typeBindings.CTD_ANON_4 = CTD_ANON_4


# Complex type [anonymous] with content type EMPTY
class CTD_ANON_5 (pyxb.binding.basis.complexTypeDefinition):
    """Suppresses a public object and its dependent objects."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 154, 24)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute target uses Python identifier target
    __target = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'target'), 'target', '__AbsentNamespace0_CTD_ANON_5_target', pyxb.binding.datatypes.string, required=True)
    __target._DeclarationLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 155, 26)
    __target._UseLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 155, 26)
    
    target = property(__target.value, __target.set, None, 'Accession or refname of the object that is being suppressed.')

    
    # Attribute HoldUntilDate uses Python identifier HoldUntilDate
    __HoldUntilDate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'HoldUntilDate'), 'HoldUntilDate', '__AbsentNamespace0_CTD_ANON_5_HoldUntilDate', pyxb.binding.datatypes.date)
    __HoldUntilDate._DeclarationLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 160, 26)
    __HoldUntilDate._UseLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 160, 26)
    
    HoldUntilDate = property(__HoldUntilDate.value, __HoldUntilDate.set, None, 'The date when a temporarily suppressed object will be made public.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __target.name() : __target,
        __HoldUntilDate.name() : __HoldUntilDate
    })
_module_typeBindings.CTD_ANON_5 = CTD_ANON_5


# Complex type [anonymous] with content type EMPTY
class CTD_ANON_6 (pyxb.binding.basis.complexTypeDefinition):
    """Kills a public object and its dependent objects."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 171, 24)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute target uses Python identifier target
    __target = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'target'), 'target', '__AbsentNamespace0_CTD_ANON_6_target', pyxb.binding.datatypes.string, required=True)
    __target._DeclarationLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 172, 26)
    __target._UseLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 172, 26)
    
    target = property(__target.value, __target.set, None, 'Accession or refname of the object that is being killed.')

    
    # Attribute HoldUntilDate uses Python identifier HoldUntilDate
    __HoldUntilDate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'HoldUntilDate'), 'HoldUntilDate', '__AbsentNamespace0_CTD_ANON_6_HoldUntilDate', pyxb.binding.datatypes.date)
    __HoldUntilDate._DeclarationLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 177, 26)
    __HoldUntilDate._UseLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 177, 26)
    
    HoldUntilDate = property(__HoldUntilDate.value, __HoldUntilDate.set, None, 'The date when a temporarily killed object will be made public.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __target.name() : __target,
        __HoldUntilDate.name() : __HoldUntilDate
    })
_module_typeBindings.CTD_ANON_6 = CTD_ANON_6


# Complex type [anonymous] with content type EMPTY
class CTD_ANON_7 (pyxb.binding.basis.complexTypeDefinition):
    """Make the object public only when the hold date expires."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 188, 24)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute target uses Python identifier target
    __target = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'target'), 'target', '__AbsentNamespace0_CTD_ANON_7_target', pyxb.binding.datatypes.string)
    __target._DeclarationLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 189, 26)
    __target._UseLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 189, 26)
    
    target = property(__target.value, __target.set, None, '\n                                    Accession or refname of the object that is being made public\n                                    when the hold date expires. If not specified then\n                                    all objects in the submission will be assigned the hold date.\n                          ')

    
    # Attribute HoldUntilDate uses Python identifier HoldUntilDate
    __HoldUntilDate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'HoldUntilDate'), 'HoldUntilDate', '__AbsentNamespace0_CTD_ANON_7_HoldUntilDate', pyxb.binding.datatypes.date)
    __HoldUntilDate._DeclarationLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 198, 26)
    __HoldUntilDate._UseLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 198, 26)
    
    HoldUntilDate = property(__HoldUntilDate.value, __HoldUntilDate.set, None, 'The date when the submission will be made public.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __target.name() : __target,
        __HoldUntilDate.name() : __HoldUntilDate
    })
_module_typeBindings.CTD_ANON_7 = CTD_ANON_7


# Complex type [anonymous] with content type EMPTY
class CTD_ANON_8 (pyxb.binding.basis.complexTypeDefinition):
    """The object will be released immediately to public."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 209, 24)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute target uses Python identifier target
    __target = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'target'), 'target', '__AbsentNamespace0_CTD_ANON_8_target', pyxb.binding.datatypes.string)
    __target._DeclarationLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 210, 26)
    __target._UseLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 210, 26)
    
    target = property(__target.value, __target.set, None, '\n                                    Accession or refname of the object that is made public.\n                                    If not specified then all objects in the submission will \n                                    made public.\n                          ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __target.name() : __target
    })
_module_typeBindings.CTD_ANON_8 = CTD_ANON_8


# Complex type [anonymous] with content type EMPTY
class CTD_ANON_9 (pyxb.binding.basis.complexTypeDefinition):
    """This action is required for data submitted to European Genome-Phenome Archive (EGA). """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 225, 24)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_9 = CTD_ANON_9


# Complex type [anonymous] with content type EMPTY
class CTD_ANON_10 (pyxb.binding.basis.complexTypeDefinition):
    """This action will rollback the submission from the database"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 231, 24)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_10 = CTD_ANON_10


# Complex type [anonymous] with content type EMPTY
class CTD_ANON_11 (pyxb.binding.basis.complexTypeDefinition):
    """Returns the receipt for a given submission alias."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 269, 24)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute target uses Python identifier target
    __target = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'target'), 'target', '__AbsentNamespace0_CTD_ANON_11_target', pyxb.binding.datatypes.string)
    __target._DeclarationLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 270, 26)
    __target._UseLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 270, 26)
    
    target = property(__target.value, __target.set, None, 'Submission alias.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __target.name() : __target
    })
_module_typeBindings.CTD_ANON_11 = CTD_ANON_11


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_12 (pyxb.binding.basis.complexTypeDefinition):
    """
            Archive created links to associated submissions.
          """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 290, 12)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element SUBMISSION_LINK uses Python identifier SUBMISSION_LINK
    __SUBMISSION_LINK = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'SUBMISSION_LINK'), 'SUBMISSION_LINK', '__AbsentNamespace0_CTD_ANON_12_SUBMISSION_LINK', True, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 292, 16), )

    
    SUBMISSION_LINK = property(__SUBMISSION_LINK.value, __SUBMISSION_LINK.set, None, None)

    _ElementMap.update({
        __SUBMISSION_LINK.name() : __SUBMISSION_LINK
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_12 = CTD_ANON_12


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_13 (pyxb.binding.basis.complexTypeDefinition):
    """
            Archive assigned properties and attributes of a SUBMISSION.  
          """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 303, 12)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element SUBMISSION_ATTRIBUTE uses Python identifier SUBMISSION_ATTRIBUTE
    __SUBMISSION_ATTRIBUTE = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'SUBMISSION_ATTRIBUTE'), 'SUBMISSION_ATTRIBUTE', '__AbsentNamespace0_CTD_ANON_13_SUBMISSION_ATTRIBUTE', True, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 305, 16), )

    
    SUBMISSION_ATTRIBUTE = property(__SUBMISSION_ATTRIBUTE.value, __SUBMISSION_ATTRIBUTE.set, None, None)

    _ElementMap.update({
        __SUBMISSION_ATTRIBUTE.name() : __SUBMISSION_ATTRIBUTE
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_13 = CTD_ANON_13


# Complex type SubmissionSetType with content type ELEMENT_ONLY
class SubmissionSetType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type SubmissionSetType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SubmissionSetType')
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 337, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element SUBMISSION uses Python identifier SUBMISSION
    __SUBMISSION = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'SUBMISSION'), 'SUBMISSION', '__AbsentNamespace0_SubmissionSetType_SUBMISSION', True, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 339, 6), )

    
    SUBMISSION = property(__SUBMISSION.value, __SUBMISSION.set, None, None)

    _ElementMap.update({
        __SUBMISSION.name() : __SUBMISSION
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.SubmissionSetType = SubmissionSetType
Namespace.addCategoryObject('typeBinding', 'SubmissionSetType', SubmissionSetType)


# Complex type SubmissionType with content type ELEMENT_ONLY
class SubmissionType (_ImportedBinding__com.ObjectType):
    """
       A Submission type is used to describe an object that contains submission actions to be performed by the archive.
    """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SubmissionType')
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 17, 2)
    _ElementMap = _ImportedBinding__com.ObjectType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__com.ObjectType._AttributeMap.copy()
    # Base type is _ImportedBinding__com.ObjectType
    
    # Element TITLE uses Python identifier TITLE
    __TITLE = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'TITLE'), 'TITLE', '__AbsentNamespace0_SubmissionType_TITLE', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 26, 10), )

    
    TITLE = property(__TITLE.value, __TITLE.set, None, '\n            Short text that can be used to define submissions in searches or in displays.\n          ')

    
    # Element CONTACTS uses Python identifier CONTACTS
    __CONTACTS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'CONTACTS'), 'CONTACTS', '__AbsentNamespace0_SubmissionType_CONTACTS', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 33, 10), )

    
    CONTACTS = property(__CONTACTS.value, __CONTACTS.set, None, None)

    
    # Element ACTIONS uses Python identifier ACTIONS
    __ACTIONS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ACTIONS'), 'ACTIONS', '__AbsentNamespace0_SubmissionType_ACTIONS', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 65, 10), )

    
    ACTIONS = property(__ACTIONS.value, __ACTIONS.set, None, None)

    
    # Element SUBMISSION_LINKS uses Python identifier SUBMISSION_LINKS
    __SUBMISSION_LINKS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'SUBMISSION_LINKS'), 'SUBMISSION_LINKS', '__AbsentNamespace0_SubmissionType_SUBMISSION_LINKS', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 284, 10), )

    
    SUBMISSION_LINKS = property(__SUBMISSION_LINKS.value, __SUBMISSION_LINKS.set, None, '\n            Archive created links to associated submissions.\n          ')

    
    # Element SUBMISSION_ATTRIBUTES uses Python identifier SUBMISSION_ATTRIBUTES
    __SUBMISSION_ATTRIBUTES = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'SUBMISSION_ATTRIBUTES'), 'SUBMISSION_ATTRIBUTES', '__AbsentNamespace0_SubmissionType_SUBMISSION_ATTRIBUTES', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 297, 10), )

    
    SUBMISSION_ATTRIBUTES = property(__SUBMISSION_ATTRIBUTES.value, __SUBMISSION_ATTRIBUTES.set, None, '\n            Archive assigned properties and attributes of a SUBMISSION.  \n          ')

    
    # Element IDENTIFIERS (IDENTIFIERS) inherited from {SRA.common}ObjectType
    
    # Attribute submission_date uses Python identifier submission_date
    __submission_date = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'submission_date'), 'submission_date', '__AbsentNamespace0_SubmissionType_submission_date', pyxb.binding.datatypes.dateTime)
    __submission_date._DeclarationLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 311, 8)
    __submission_date._UseLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 311, 8)
    
    submission_date = property(__submission_date.value, __submission_date.set, None, '\n          Submitter assigned preparation date of this submission object.\n        ')

    
    # Attribute submission_comment uses Python identifier submission_comment
    __submission_comment = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'submission_comment'), 'submission_comment', '__AbsentNamespace0_SubmissionType_submission_comment', pyxb.binding.datatypes.string)
    __submission_comment._DeclarationLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 318, 8)
    __submission_comment._UseLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 318, 8)
    
    submission_comment = property(__submission_comment.value, __submission_comment.set, None, '\n          Submitter assigned comment.\n        ')

    
    # Attribute lab_name uses Python identifier lab_name
    __lab_name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'lab_name'), 'lab_name', '__AbsentNamespace0_SubmissionType_lab_name', pyxb.binding.datatypes.string)
    __lab_name._DeclarationLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 325, 8)
    __lab_name._UseLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 325, 8)
    
    lab_name = property(__lab_name.value, __lab_name.set, None, '\n          Laboratory name within submitting institution.\n        ')

    
    # Attribute alias inherited from {SRA.common}ObjectType
    
    # Attribute center_name inherited from {SRA.common}ObjectType
    
    # Attribute broker_name inherited from {SRA.common}ObjectType
    
    # Attribute accession inherited from {SRA.common}ObjectType
    _ElementMap.update({
        __TITLE.name() : __TITLE,
        __CONTACTS.name() : __CONTACTS,
        __ACTIONS.name() : __ACTIONS,
        __SUBMISSION_LINKS.name() : __SUBMISSION_LINKS,
        __SUBMISSION_ATTRIBUTES.name() : __SUBMISSION_ATTRIBUTES
    })
    _AttributeMap.update({
        __submission_date.name() : __submission_date,
        __submission_comment.name() : __submission_comment,
        __lab_name.name() : __lab_name
    })
_module_typeBindings.SubmissionType = SubmissionType
Namespace.addCategoryObject('typeBinding', 'SubmissionType', SubmissionType)


# Complex type [anonymous] with content type EMPTY
class CTD_ANON_14 (pyxb.binding.basis.complexTypeDefinition):
    """Add an object to the archive."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 78, 24)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute source uses Python identifier source
    __source = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'source'), 'source', '__AbsentNamespace0_CTD_ANON_14_source', pyxb.binding.datatypes.string)
    __source._DeclarationLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 79, 26)
    __source._UseLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 79, 26)
    
    source = property(__source.value, __source.set, None, 'Filename or relative path to the XML file being submitted.')

    
    # Attribute schema uses Python identifier schema
    __schema = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'schema'), 'schema', '__AbsentNamespace0_CTD_ANON_14_schema', _module_typeBindings.STD_ANON)
    __schema._DeclarationLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 84, 26)
    __schema._UseLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 84, 26)
    
    schema = property(__schema.value, __schema.set, None, 'The type of the XML file being submitted.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __source.name() : __source,
        __schema.name() : __schema
    })
_module_typeBindings.CTD_ANON_14 = CTD_ANON_14


# Complex type [anonymous] with content type EMPTY
class CTD_ANON_15 (pyxb.binding.basis.complexTypeDefinition):
    """Modify an object in the archive."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 110, 24)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute source uses Python identifier source
    __source = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'source'), 'source', '__AbsentNamespace0_CTD_ANON_15_source', pyxb.binding.datatypes.string)
    __source._DeclarationLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 111, 26)
    __source._UseLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 111, 26)
    
    source = property(__source.value, __source.set, None, 'Filename or relative path to the XML file being updated.')

    
    # Attribute schema uses Python identifier schema
    __schema = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'schema'), 'schema', '__AbsentNamespace0_CTD_ANON_15_schema', _module_typeBindings.STD_ANON_)
    __schema._DeclarationLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 116, 26)
    __schema._UseLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 116, 26)
    
    schema = property(__schema.value, __schema.set, None, 'The type of the XML file being updated.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __source.name() : __source,
        __schema.name() : __schema
    })
_module_typeBindings.CTD_ANON_15 = CTD_ANON_15


# Complex type [anonymous] with content type EMPTY
class CTD_ANON_16 (pyxb.binding.basis.complexTypeDefinition):
    """Validates the submitted XMLs without actually submitting them."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 237, 24)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute source uses Python identifier source
    __source = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'source'), 'source', '__AbsentNamespace0_CTD_ANON_16_source', pyxb.binding.datatypes.string)
    __source._DeclarationLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 238, 26)
    __source._UseLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 238, 26)
    
    source = property(__source.value, __source.set, None, 'Filename or relative path to the XML file being validated.')

    
    # Attribute schema uses Python identifier schema
    __schema = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'schema'), 'schema', '__AbsentNamespace0_CTD_ANON_16_schema', _module_typeBindings.STD_ANON_2)
    __schema._DeclarationLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 243, 26)
    __schema._UseLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 243, 26)
    
    schema = property(__schema.value, __schema.set, None, 'The type of the XML file being validated.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __source.name() : __source,
        __schema.name() : __schema
    })
_module_typeBindings.CTD_ANON_16 = CTD_ANON_16


SUBMISSION_SET = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SUBMISSION_SET'), SubmissionSetType, documentation='\n      An SUBMISSION_SET is a container for a set of studies and a common namespace.\n    ', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 343, 2))
Namespace.addCategoryObject('elementBinding', SUBMISSION_SET.name().localName(), SUBMISSION_SET)

SUBMISSION = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SUBMISSION'), SubmissionType, location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 352, 2))
Namespace.addCategoryObject('elementBinding', SUBMISSION.name().localName(), SUBMISSION)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'CONTACT'), CTD_ANON_, scope=CTD_ANON, location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 36, 16)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'CONTACT')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 36, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton()




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ACTION'), CTD_ANON_3, scope=CTD_ANON_2, documentation='Action to be executed by the archive.', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 68, 16)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(None, 'ACTION')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 68, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_2._Automaton = _BuildAutomaton_()




CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ADD'), CTD_ANON_14, scope=CTD_ANON_3, documentation='Add an object to the archive.', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 74, 22)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'MODIFY'), CTD_ANON_15, scope=CTD_ANON_3, documentation='Modify an object in the archive.', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 106, 22)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'CANCEL'), CTD_ANON_4, scope=CTD_ANON_3, documentation='Cancels a private object and its dependent objects.', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 138, 22)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'SUPPRESS'), CTD_ANON_5, scope=CTD_ANON_3, documentation='Suppresses a public object and its dependent objects.', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 150, 22)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'KILL'), CTD_ANON_6, scope=CTD_ANON_3, documentation='Kills a public object and its dependent objects.', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 167, 22)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'HOLD'), CTD_ANON_7, scope=CTD_ANON_3, documentation='Make the object public only when the hold date expires.', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 184, 22)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'RELEASE'), CTD_ANON_8, scope=CTD_ANON_3, documentation='The object will be released immediately to public.', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 205, 22)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'PROTECT'), CTD_ANON_9, scope=CTD_ANON_3, documentation='This action is required for data submitted to European Genome-Phenome Archive (EGA). ', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 221, 22)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ROLLBACK'), CTD_ANON_10, scope=CTD_ANON_3, documentation='This action will rollback the submission from the database', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 227, 22)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'VALIDATE'), CTD_ANON_16, scope=CTD_ANON_3, documentation='Validates the submitted XMLs without actually submitting them.', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 233, 22)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'RECEIPT'), CTD_ANON_11, scope=CTD_ANON_3, documentation='Returns the receipt for a given submission alias.', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 265, 22)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(None, 'ADD')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 74, 22))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(None, 'MODIFY')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 106, 22))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(None, 'CANCEL')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 138, 22))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(None, 'SUPPRESS')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 150, 22))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(None, 'KILL')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 167, 22))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(None, 'HOLD')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 184, 22))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(None, 'RELEASE')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 205, 22))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(None, 'PROTECT')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 221, 22))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(None, 'ROLLBACK')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 227, 22))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(None, 'VALIDATE')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 233, 22))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(None, 'RECEIPT')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 265, 22))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
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
    transitions = []
    st_10._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_3._Automaton = _BuildAutomaton_2()




CTD_ANON_12._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'SUBMISSION_LINK'), _ImportedBinding__com.LinkType, scope=CTD_ANON_12, location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 292, 16)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(None, 'SUBMISSION_LINK')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 292, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_12._Automaton = _BuildAutomaton_3()




CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'SUBMISSION_ATTRIBUTE'), _ImportedBinding__com.AttributeType, scope=CTD_ANON_13, location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 305, 16)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(None, 'SUBMISSION_ATTRIBUTE')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 305, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_13._Automaton = _BuildAutomaton_4()




SubmissionSetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'SUBMISSION'), SubmissionType, scope=SubmissionSetType, location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 339, 6)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SubmissionSetType._UseForTag(pyxb.namespace.ExpandedName(None, 'SUBMISSION')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 339, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
SubmissionSetType._Automaton = _BuildAutomaton_5()




SubmissionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'TITLE'), pyxb.binding.datatypes.string, scope=SubmissionType, documentation='\n            Short text that can be used to define submissions in searches or in displays.\n          ', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 26, 10)))

SubmissionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'CONTACTS'), CTD_ANON, scope=SubmissionType, location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 33, 10)))

SubmissionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ACTIONS'), CTD_ANON_2, scope=SubmissionType, location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 65, 10)))

SubmissionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'SUBMISSION_LINKS'), CTD_ANON_12, scope=SubmissionType, documentation='\n            Archive created links to associated submissions.\n          ', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 284, 10)))

SubmissionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'SUBMISSION_ATTRIBUTES'), CTD_ANON_13, scope=SubmissionType, documentation='\n            Archive assigned properties and attributes of a SUBMISSION.  \n          ', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 297, 10)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 19, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 26, 10))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 33, 10))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 65, 10))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 284, 10))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 297, 10))
    counters.add(cc_5)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SubmissionType._UseForTag(pyxb.namespace.ExpandedName(None, 'IDENTIFIERS')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 19, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(SubmissionType._UseForTag(pyxb.namespace.ExpandedName(None, 'TITLE')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 26, 10))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(SubmissionType._UseForTag(pyxb.namespace.ExpandedName(None, 'CONTACTS')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 33, 10))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(SubmissionType._UseForTag(pyxb.namespace.ExpandedName(None, 'ACTIONS')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 65, 10))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(SubmissionType._UseForTag(pyxb.namespace.ExpandedName(None, 'SUBMISSION_LINKS')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 284, 10))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(SubmissionType._UseForTag(pyxb.namespace.ExpandedName(None, 'SUBMISSION_ATTRIBUTES')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd', 297, 10))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
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
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
SubmissionType._Automaton = _BuildAutomaton_6()

