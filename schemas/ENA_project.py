# ./ENA_project.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2019-06-06 19:25:10.525905 by PyXB version 1.2.6 using Python 3.6.7.final.0
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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:087d93ac-8880-11e9-9350-b0c090509cda')

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


# Complex type OrganismType with content type ELEMENT_ONLY
class OrganismType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type OrganismType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'OrganismType')
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 16, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element TAXON_ID uses Python identifier TAXON_ID
    __TAXON_ID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'TAXON_ID'), 'TAXON_ID', '__AbsentNamespace0_OrganismType_TAXON_ID', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 18, 12), )

    
    TAXON_ID = property(__TAXON_ID.value, __TAXON_ID.set, None, '')

    
    # Element SCIENTIFIC_NAME uses Python identifier SCIENTIFIC_NAME
    __SCIENTIFIC_NAME = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'SCIENTIFIC_NAME'), 'SCIENTIFIC_NAME', '__AbsentNamespace0_OrganismType_SCIENTIFIC_NAME', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 23, 12), )

    
    SCIENTIFIC_NAME = property(__SCIENTIFIC_NAME.value, __SCIENTIFIC_NAME.set, None, '')

    
    # Element COMMON_NAME uses Python identifier COMMON_NAME
    __COMMON_NAME = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'COMMON_NAME'), 'COMMON_NAME', '__AbsentNamespace0_OrganismType_COMMON_NAME', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 28, 12), )

    
    COMMON_NAME = property(__COMMON_NAME.value, __COMMON_NAME.set, None, '')

    
    # Element STRAIN uses Python identifier STRAIN
    __STRAIN = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'STRAIN'), 'STRAIN', '__AbsentNamespace0_OrganismType_STRAIN', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 33, 12), )

    
    STRAIN = property(__STRAIN.value, __STRAIN.set, None, None)

    
    # Element BREED uses Python identifier BREED
    __BREED = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'BREED'), 'BREED', '__AbsentNamespace0_OrganismType_BREED', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 34, 12), )

    
    BREED = property(__BREED.value, __BREED.set, None, None)

    
    # Element CULTIVAR uses Python identifier CULTIVAR
    __CULTIVAR = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'CULTIVAR'), 'CULTIVAR', '__AbsentNamespace0_OrganismType_CULTIVAR', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 35, 12), )

    
    CULTIVAR = property(__CULTIVAR.value, __CULTIVAR.set, None, None)

    
    # Element ISOLATE uses Python identifier ISOLATE
    __ISOLATE = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ISOLATE'), 'ISOLATE', '__AbsentNamespace0_OrganismType_ISOLATE', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 36, 12), )

    
    ISOLATE = property(__ISOLATE.value, __ISOLATE.set, None, None)

    _ElementMap.update({
        __TAXON_ID.name() : __TAXON_ID,
        __SCIENTIFIC_NAME.name() : __SCIENTIFIC_NAME,
        __COMMON_NAME.name() : __COMMON_NAME,
        __STRAIN.name() : __STRAIN,
        __BREED.name() : __BREED,
        __CULTIVAR.name() : __CULTIVAR,
        __ISOLATE.name() : __ISOLATE
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.OrganismType = OrganismType
Namespace.addCategoryObject('typeBinding', 'OrganismType', OrganismType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 64, 24)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element COLLABORATOR uses Python identifier COLLABORATOR
    __COLLABORATOR = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'COLLABORATOR'), 'COLLABORATOR', '__AbsentNamespace0_CTD_ANON_COLLABORATOR', True, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 66, 32), )

    
    COLLABORATOR = property(__COLLABORATOR.value, __COLLABORATOR.set, None, None)

    _ElementMap.update({
        __COLLABORATOR.name() : __COLLABORATOR
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON = CTD_ANON


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """ A project for grouping submitted data together.
                        """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 77, 28)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element SEQUENCING_PROJECT uses Python identifier SEQUENCING_PROJECT
    __SEQUENCING_PROJECT = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'SEQUENCING_PROJECT'), 'SEQUENCING_PROJECT', '__AbsentNamespace0_CTD_ANON__SEQUENCING_PROJECT', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 80, 40), )

    
    SEQUENCING_PROJECT = property(__SEQUENCING_PROJECT.value, __SEQUENCING_PROJECT.set, None, None)

    
    # Element ORGANISM uses Python identifier ORGANISM
    __ORGANISM = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ORGANISM'), 'ORGANISM', '__AbsentNamespace0_CTD_ANON__ORGANISM', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 89, 36), )

    
    ORGANISM = property(__ORGANISM.value, __ORGANISM.set, None, None)

    _ElementMap.update({
        __SEQUENCING_PROJECT.name() : __SEQUENCING_PROJECT,
        __ORGANISM.name() : __ORGANISM
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_ = CTD_ANON_


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 81, 44)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element LOCUS_TAG_PREFIX uses Python identifier LOCUS_TAG_PREFIX
    __LOCUS_TAG_PREFIX = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'LOCUS_TAG_PREFIX'), 'LOCUS_TAG_PREFIX', '__AbsentNamespace0_CTD_ANON_2_LOCUS_TAG_PREFIX', True, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 83, 50), )

    
    LOCUS_TAG_PREFIX = property(__LOCUS_TAG_PREFIX.value, __LOCUS_TAG_PREFIX.set, None, None)

    _ElementMap.update({
        __LOCUS_TAG_PREFIX.name() : __LOCUS_TAG_PREFIX
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_2 = CTD_ANON_2


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    """ A project for grouping other projects together.
                        """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 99, 28)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element ORGANISM uses Python identifier ORGANISM
    __ORGANISM = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ORGANISM'), 'ORGANISM', '__AbsentNamespace0_CTD_ANON_3_ORGANISM', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 101, 36), )

    
    ORGANISM = property(__ORGANISM.value, __ORGANISM.set, None, None)

    _ElementMap.update({
        __ORGANISM.name() : __ORGANISM
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_3 = CTD_ANON_3


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_4 (pyxb.binding.basis.complexTypeDefinition):
    """ Other projects related to this project. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 111, 24)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element RELATED_PROJECT uses Python identifier RELATED_PROJECT
    __RELATED_PROJECT = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'RELATED_PROJECT'), 'RELATED_PROJECT', '__AbsentNamespace0_CTD_ANON_4_RELATED_PROJECT', True, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 113, 32), )

    
    RELATED_PROJECT = property(__RELATED_PROJECT.value, __RELATED_PROJECT.set, None, None)

    _ElementMap.update({
        __RELATED_PROJECT.name() : __RELATED_PROJECT
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_4 = CTD_ANON_4


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_5 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 114, 36)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element PARENT_PROJECT uses Python identifier PARENT_PROJECT
    __PARENT_PROJECT = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'PARENT_PROJECT'), 'PARENT_PROJECT', '__AbsentNamespace0_CTD_ANON_5_PARENT_PROJECT', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 116, 44), )

    
    PARENT_PROJECT = property(__PARENT_PROJECT.value, __PARENT_PROJECT.set, None, None)

    
    # Element CHILD_PROJECT uses Python identifier CHILD_PROJECT
    __CHILD_PROJECT = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'CHILD_PROJECT'), 'CHILD_PROJECT', '__AbsentNamespace0_CTD_ANON_5_CHILD_PROJECT', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 127, 44), )

    
    CHILD_PROJECT = property(__CHILD_PROJECT.value, __CHILD_PROJECT.set, None, None)

    
    # Element PEER_PROJECT uses Python identifier PEER_PROJECT
    __PEER_PROJECT = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'PEER_PROJECT'), 'PEER_PROJECT', '__AbsentNamespace0_CTD_ANON_5_PEER_PROJECT', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 138, 44), )

    
    PEER_PROJECT = property(__PEER_PROJECT.value, __PEER_PROJECT.set, None, None)

    _ElementMap.update({
        __PARENT_PROJECT.name() : __PARENT_PROJECT,
        __CHILD_PROJECT.name() : __CHILD_PROJECT,
        __PEER_PROJECT.name() : __PEER_PROJECT
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_5 = CTD_ANON_5


# Complex type [anonymous] with content type EMPTY
class CTD_ANON_6 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 117, 48)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute accession uses Python identifier accession
    __accession = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'accession'), 'accession', '__AbsentNamespace0_CTD_ANON_6_accession', pyxb.binding.datatypes.string, required=True)
    __accession._DeclarationLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 118, 50)
    __accession._UseLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 118, 50)
    
    accession = property(__accession.value, __accession.set, None, ' Identifies the project using\n                                                 an accession number. ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __accession.name() : __accession
    })
_module_typeBindings.CTD_ANON_6 = CTD_ANON_6


# Complex type [anonymous] with content type EMPTY
class CTD_ANON_7 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 128, 48)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute accession uses Python identifier accession
    __accession = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'accession'), 'accession', '__AbsentNamespace0_CTD_ANON_7_accession', pyxb.binding.datatypes.string, required=True)
    __accession._DeclarationLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 129, 50)
    __accession._UseLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 129, 50)
    
    accession = property(__accession.value, __accession.set, None, ' Identifies the project using\n                                                 an accession number. ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __accession.name() : __accession
    })
_module_typeBindings.CTD_ANON_7 = CTD_ANON_7


# Complex type [anonymous] with content type EMPTY
class CTD_ANON_8 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 139, 48)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute accession uses Python identifier accession
    __accession = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'accession'), 'accession', '__AbsentNamespace0_CTD_ANON_8_accession', pyxb.binding.datatypes.string, required=True)
    __accession._DeclarationLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 140, 50)
    __accession._UseLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 140, 50)
    
    accession = property(__accession.value, __accession.set, None, ' Identifies the project using\n                                                 an accession number. ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __accession.name() : __accession
    })
_module_typeBindings.CTD_ANON_8 = CTD_ANON_8


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_9 (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 159, 24)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element PROJECT_LINK uses Python identifier PROJECT_LINK
    __PROJECT_LINK = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'PROJECT_LINK'), 'PROJECT_LINK', '__AbsentNamespace0_CTD_ANON_9_PROJECT_LINK', True, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 161, 32), )

    
    PROJECT_LINK = property(__PROJECT_LINK.value, __PROJECT_LINK.set, None, None)

    _ElementMap.update({
        __PROJECT_LINK.name() : __PROJECT_LINK
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_9 = CTD_ANON_9


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_10 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 162, 36)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element XREF_LINK uses Python identifier XREF_LINK
    __XREF_LINK = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'XREF_LINK'), 'XREF_LINK', '__AbsentNamespace0_CTD_ANON_10_XREF_LINK', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 164, 44), )

    
    XREF_LINK = property(__XREF_LINK.value, __XREF_LINK.set, None, None)

    
    # Element URL_LINK uses Python identifier URL_LINK
    __URL_LINK = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'URL_LINK'), 'URL_LINK', '__AbsentNamespace0_CTD_ANON_10_URL_LINK', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 165, 44), )

    
    URL_LINK = property(__URL_LINK.value, __URL_LINK.set, None, None)

    _ElementMap.update({
        __XREF_LINK.name() : __XREF_LINK,
        __URL_LINK.name() : __URL_LINK
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
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 177, 24)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element PROJECT_ATTRIBUTE uses Python identifier PROJECT_ATTRIBUTE
    __PROJECT_ATTRIBUTE = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'PROJECT_ATTRIBUTE'), 'PROJECT_ATTRIBUTE', '__AbsentNamespace0_CTD_ANON_11_PROJECT_ATTRIBUTE', True, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 179, 32), )

    
    PROJECT_ATTRIBUTE = property(__PROJECT_ATTRIBUTE.value, __PROJECT_ATTRIBUTE.set, None, None)

    _ElementMap.update({
        __PROJECT_ATTRIBUTE.name() : __PROJECT_ATTRIBUTE
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_11 = CTD_ANON_11


# Complex type ProjectSetType with content type ELEMENT_ONLY
class ProjectSetType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type ProjectSetType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ProjectSetType')
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 192, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element PROJECT uses Python identifier PROJECT
    __PROJECT = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'PROJECT'), 'PROJECT', '__AbsentNamespace0_ProjectSetType_PROJECT', True, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 194, 12), )

    
    PROJECT = property(__PROJECT.value, __PROJECT.set, None, None)

    _ElementMap.update({
        __PROJECT.name() : __PROJECT
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ProjectSetType = ProjectSetType
Namespace.addCategoryObject('typeBinding', 'ProjectSetType', ProjectSetType)


# Complex type ProjectType with content type ELEMENT_ONLY
class ProjectType (_ImportedBinding__com.ObjectType):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ProjectType')
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 39, 4)
    _ElementMap = _ImportedBinding__com.ObjectType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__com.ObjectType._AttributeMap.copy()
    # Base type is _ImportedBinding__com.ObjectType
    
    # Element NAME uses Python identifier NAME
    __NAME = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'NAME'), 'NAME', '__AbsentNamespace0_ProjectType_NAME', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 46, 20), )

    
    NAME = property(__NAME.value, __NAME.set, None, ' A short name of the project. ')

    
    # Element TITLE uses Python identifier TITLE
    __TITLE = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'TITLE'), 'TITLE', '__AbsentNamespace0_ProjectType_TITLE', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 51, 20), )

    
    TITLE = property(__TITLE.value, __TITLE.set, None, ' A short descriptive title for the project.\n                    ')

    
    # Element DESCRIPTION uses Python identifier DESCRIPTION
    __DESCRIPTION = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'DESCRIPTION'), 'DESCRIPTION', '__AbsentNamespace0_ProjectType_DESCRIPTION', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 57, 20), )

    
    DESCRIPTION = property(__DESCRIPTION.value, __DESCRIPTION.set, None, ' A long description of the scope of the project.\n                    ')

    
    # Element COLLABORATORS uses Python identifier COLLABORATORS
    __COLLABORATORS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'COLLABORATORS'), 'COLLABORATORS', '__AbsentNamespace0_ProjectType_COLLABORATORS', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 63, 20), )

    
    COLLABORATORS = property(__COLLABORATORS.value, __COLLABORATORS.set, None, None)

    
    # Element SUBMISSION_PROJECT uses Python identifier SUBMISSION_PROJECT
    __SUBMISSION_PROJECT = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'SUBMISSION_PROJECT'), 'SUBMISSION_PROJECT', '__AbsentNamespace0_ProjectType_SUBMISSION_PROJECT', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 72, 24), )

    
    SUBMISSION_PROJECT = property(__SUBMISSION_PROJECT.value, __SUBMISSION_PROJECT.set, None, ' A project for grouping submitted data together.\n                        ')

    
    # Element UMBRELLA_PROJECT uses Python identifier UMBRELLA_PROJECT
    __UMBRELLA_PROJECT = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'UMBRELLA_PROJECT'), 'UMBRELLA_PROJECT', '__AbsentNamespace0_ProjectType_UMBRELLA_PROJECT', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 94, 24), )

    
    UMBRELLA_PROJECT = property(__UMBRELLA_PROJECT.value, __UMBRELLA_PROJECT.set, None, ' A project for grouping other projects together.\n                        ')

    
    # Element RELATED_PROJECTS uses Python identifier RELATED_PROJECTS
    __RELATED_PROJECTS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'RELATED_PROJECTS'), 'RELATED_PROJECTS', '__AbsentNamespace0_ProjectType_RELATED_PROJECTS', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 107, 20), )

    
    RELATED_PROJECTS = property(__RELATED_PROJECTS.value, __RELATED_PROJECTS.set, None, ' Other projects related to this project. ')

    
    # Element PROJECT_LINKS uses Python identifier PROJECT_LINKS
    __PROJECT_LINKS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'PROJECT_LINKS'), 'PROJECT_LINKS', '__AbsentNamespace0_ProjectType_PROJECT_LINKS', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 155, 20), )

    
    PROJECT_LINKS = property(__PROJECT_LINKS.value, __PROJECT_LINKS.set, None, '')

    
    # Element PROJECT_ATTRIBUTES uses Python identifier PROJECT_ATTRIBUTES
    __PROJECT_ATTRIBUTES = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'PROJECT_ATTRIBUTES'), 'PROJECT_ATTRIBUTES', '__AbsentNamespace0_ProjectType_PROJECT_ATTRIBUTES', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 173, 20), )

    
    PROJECT_ATTRIBUTES = property(__PROJECT_ATTRIBUTES.value, __PROJECT_ATTRIBUTES.set, None, '')

    
    # Element IDENTIFIERS (IDENTIFIERS) inherited from {SRA.common}ObjectType
    
    # Attribute first_public uses Python identifier first_public
    __first_public = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'first_public'), 'first_public', '__AbsentNamespace0_ProjectType_first_public', pyxb.binding.datatypes.date)
    __first_public._DeclarationLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 184, 16)
    __first_public._UseLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 184, 16)
    
    first_public = property(__first_public.value, __first_public.set, None, '')

    
    # Attribute alias inherited from {SRA.common}ObjectType
    
    # Attribute center_name inherited from {SRA.common}ObjectType
    
    # Attribute broker_name inherited from {SRA.common}ObjectType
    
    # Attribute accession inherited from {SRA.common}ObjectType
    _ElementMap.update({
        __NAME.name() : __NAME,
        __TITLE.name() : __TITLE,
        __DESCRIPTION.name() : __DESCRIPTION,
        __COLLABORATORS.name() : __COLLABORATORS,
        __SUBMISSION_PROJECT.name() : __SUBMISSION_PROJECT,
        __UMBRELLA_PROJECT.name() : __UMBRELLA_PROJECT,
        __RELATED_PROJECTS.name() : __RELATED_PROJECTS,
        __PROJECT_LINKS.name() : __PROJECT_LINKS,
        __PROJECT_ATTRIBUTES.name() : __PROJECT_ATTRIBUTES
    })
    _AttributeMap.update({
        __first_public.name() : __first_public
    })
_module_typeBindings.ProjectType = ProjectType
Namespace.addCategoryObject('typeBinding', 'ProjectType', ProjectType)


PROJECT_SET = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PROJECT_SET'), ProjectSetType, documentation='', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 197, 4))
Namespace.addCategoryObject('elementBinding', PROJECT_SET.name().localName(), PROJECT_SET)

PROJECT = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PROJECT'), ProjectType, location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 202, 4))
Namespace.addCategoryObject('elementBinding', PROJECT.name().localName(), PROJECT)



OrganismType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'TAXON_ID'), pyxb.binding.datatypes.int, scope=OrganismType, documentation='', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 18, 12)))

OrganismType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'SCIENTIFIC_NAME'), pyxb.binding.datatypes.string, scope=OrganismType, documentation='', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 23, 12)))

OrganismType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'COMMON_NAME'), pyxb.binding.datatypes.string, scope=OrganismType, documentation='', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 28, 12)))

OrganismType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'STRAIN'), pyxb.binding.datatypes.string, scope=OrganismType, location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 33, 12)))

OrganismType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'BREED'), pyxb.binding.datatypes.string, scope=OrganismType, location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 34, 12)))

OrganismType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'CULTIVAR'), pyxb.binding.datatypes.string, scope=OrganismType, location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 35, 12)))

OrganismType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ISOLATE'), pyxb.binding.datatypes.string, scope=OrganismType, location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 36, 12)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(OrganismType._UseForTag(pyxb.namespace.ExpandedName(None, 'TAXON_ID')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 18, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=st_0)

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(OrganismType._UseForTag(pyxb.namespace.ExpandedName(None, 'SCIENTIFIC_NAME')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 23, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=st_0)

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 28, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(OrganismType._UseForTag(pyxb.namespace.ExpandedName(None, 'COMMON_NAME')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 28, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 33, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(OrganismType._UseForTag(pyxb.namespace.ExpandedName(None, 'STRAIN')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 33, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 34, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(OrganismType._UseForTag(pyxb.namespace.ExpandedName(None, 'BREED')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 34, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 35, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(OrganismType._UseForTag(pyxb.namespace.ExpandedName(None, 'CULTIVAR')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 35, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 36, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(OrganismType._UseForTag(pyxb.namespace.ExpandedName(None, 'ISOLATE')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 36, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 28, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 33, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 34, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 35, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 36, 12))
    counters.add(cc_4)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_())
    sub_automata.append(_BuildAutomaton_2())
    sub_automata.append(_BuildAutomaton_3())
    sub_automata.append(_BuildAutomaton_4())
    sub_automata.append(_BuildAutomaton_5())
    sub_automata.append(_BuildAutomaton_6())
    sub_automata.append(_BuildAutomaton_7())
    final_update = set()
    symbol = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 17, 8)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
OrganismType._Automaton = _BuildAutomaton()




CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'COLLABORATOR'), pyxb.binding.datatypes.string, scope=CTD_ANON, location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 66, 32)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'COLLABORATOR')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 66, 32))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton_8()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'SEQUENCING_PROJECT'), CTD_ANON_2, scope=CTD_ANON_, location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 80, 40)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ORGANISM'), OrganismType, scope=CTD_ANON_, location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 89, 36)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 89, 36))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, 'SEQUENCING_PROJECT')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 80, 40))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, 'ORGANISM')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 89, 36))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_9()




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'LOCUS_TAG_PREFIX'), pyxb.binding.datatypes.token, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 83, 50)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 83, 50))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(None, 'LOCUS_TAG_PREFIX')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 83, 50))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_2._Automaton = _BuildAutomaton_10()




CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ORGANISM'), OrganismType, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 101, 36)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 101, 36))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(None, 'ORGANISM')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 101, 36))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_3._Automaton = _BuildAutomaton_11()




CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'RELATED_PROJECT'), CTD_ANON_5, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 113, 32)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(None, 'RELATED_PROJECT')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 113, 32))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_4._Automaton = _BuildAutomaton_12()




CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'PARENT_PROJECT'), CTD_ANON_6, scope=CTD_ANON_5, location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 116, 44)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'CHILD_PROJECT'), CTD_ANON_7, scope=CTD_ANON_5, location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 127, 44)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'PEER_PROJECT'), CTD_ANON_8, scope=CTD_ANON_5, location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 138, 44)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(None, 'PARENT_PROJECT')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 116, 44))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(None, 'CHILD_PROJECT')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 127, 44))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(None, 'PEER_PROJECT')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 138, 44))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_5._Automaton = _BuildAutomaton_13()




CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'PROJECT_LINK'), CTD_ANON_10, scope=CTD_ANON_9, location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 161, 32)))

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(None, 'PROJECT_LINK')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 161, 32))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_9._Automaton = _BuildAutomaton_14()




CTD_ANON_10._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'XREF_LINK'), _ImportedBinding__com.XRefType, scope=CTD_ANON_10, location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 164, 44)))

CTD_ANON_10._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'URL_LINK'), _ImportedBinding__com.URLType, scope=CTD_ANON_10, location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 165, 44)))

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(None, 'XREF_LINK')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 164, 44))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(None, 'URL_LINK')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 165, 44))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_10._Automaton = _BuildAutomaton_15()




CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'PROJECT_ATTRIBUTE'), _ImportedBinding__com.AttributeType, scope=CTD_ANON_11, location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 179, 32)))

def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(None, 'PROJECT_ATTRIBUTE')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 179, 32))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_11._Automaton = _BuildAutomaton_16()




ProjectSetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'PROJECT'), ProjectType, scope=ProjectSetType, location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 194, 12)))

def _BuildAutomaton_17 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ProjectSetType._UseForTag(pyxb.namespace.ExpandedName(None, 'PROJECT')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 194, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ProjectSetType._Automaton = _BuildAutomaton_17()




ProjectType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'NAME'), pyxb.binding.datatypes.string, scope=ProjectType, documentation=' A short name of the project. ', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 46, 20)))

ProjectType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'TITLE'), pyxb.binding.datatypes.string, scope=ProjectType, documentation=' A short descriptive title for the project.\n                    ', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 51, 20)))

ProjectType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'DESCRIPTION'), pyxb.binding.datatypes.string, scope=ProjectType, documentation=' A long description of the scope of the project.\n                    ', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 57, 20)))

ProjectType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'COLLABORATORS'), CTD_ANON, scope=ProjectType, location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 63, 20)))

ProjectType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'SUBMISSION_PROJECT'), CTD_ANON_, scope=ProjectType, documentation=' A project for grouping submitted data together.\n                        ', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 72, 24)))

ProjectType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'UMBRELLA_PROJECT'), CTD_ANON_3, scope=ProjectType, documentation=' A project for grouping other projects together.\n                        ', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 94, 24)))

ProjectType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'RELATED_PROJECTS'), CTD_ANON_4, scope=ProjectType, documentation=' Other projects related to this project. ', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 107, 20)))

ProjectType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'PROJECT_LINKS'), CTD_ANON_9, scope=ProjectType, documentation='', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 155, 20)))

ProjectType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'PROJECT_ATTRIBUTES'), CTD_ANON_11, scope=ProjectType, documentation='', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 173, 20)))

def _BuildAutomaton_18 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 19, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 46, 20))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 57, 20))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 63, 20))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 107, 20))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 155, 20))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 173, 20))
    counters.add(cc_6)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ProjectType._UseForTag(pyxb.namespace.ExpandedName(None, 'IDENTIFIERS')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 19, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ProjectType._UseForTag(pyxb.namespace.ExpandedName(None, 'NAME')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 46, 20))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ProjectType._UseForTag(pyxb.namespace.ExpandedName(None, 'TITLE')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 51, 20))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ProjectType._UseForTag(pyxb.namespace.ExpandedName(None, 'DESCRIPTION')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 57, 20))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ProjectType._UseForTag(pyxb.namespace.ExpandedName(None, 'COLLABORATORS')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 63, 20))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ProjectType._UseForTag(pyxb.namespace.ExpandedName(None, 'SUBMISSION_PROJECT')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 72, 24))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ProjectType._UseForTag(pyxb.namespace.ExpandedName(None, 'UMBRELLA_PROJECT')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 94, 24))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(ProjectType._UseForTag(pyxb.namespace.ExpandedName(None, 'RELATED_PROJECTS')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 107, 20))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(ProjectType._UseForTag(pyxb.namespace.ExpandedName(None, 'PROJECT_LINKS')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 155, 20))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(ProjectType._UseForTag(pyxb.namespace.ExpandedName(None, 'PROJECT_ATTRIBUTES')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/ENA.project.xsd', 173, 20))
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
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, True) ]))
    st_9._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ProjectType._Automaton = _BuildAutomaton_18()

