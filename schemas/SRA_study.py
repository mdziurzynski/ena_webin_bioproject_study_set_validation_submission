# ./SRA_study.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2019-06-06 19:25:19.333705 by PyXB version 1.2.6 using Python 3.6.7.final.0
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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:0dc55976-8880-11e9-9350-b0c090509cda')

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
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.study.xsd', 45, 22)
    _Documentation = None
STD_ANON._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON, enum_prefix=None)
STD_ANON.Whole_Genome_Sequencing = STD_ANON._CF_enumeration.addEnumeration(unicode_value='Whole Genome Sequencing', tag='Whole_Genome_Sequencing')
STD_ANON.Metagenomics = STD_ANON._CF_enumeration.addEnumeration(unicode_value='Metagenomics', tag='Metagenomics')
STD_ANON.Transcriptome_Analysis = STD_ANON._CF_enumeration.addEnumeration(unicode_value='Transcriptome Analysis', tag='Transcriptome_Analysis')
STD_ANON.Resequencing = STD_ANON._CF_enumeration.addEnumeration(unicode_value='Resequencing', tag='Resequencing')
STD_ANON.Epigenetics = STD_ANON._CF_enumeration.addEnumeration(unicode_value='Epigenetics', tag='Epigenetics')
STD_ANON.Synthetic_Genomics = STD_ANON._CF_enumeration.addEnumeration(unicode_value='Synthetic Genomics', tag='Synthetic_Genomics')
STD_ANON.Forensic_or_Paleo_genomics = STD_ANON._CF_enumeration.addEnumeration(unicode_value='Forensic or Paleo-genomics', tag='Forensic_or_Paleo_genomics')
STD_ANON.Gene_Regulation_Study = STD_ANON._CF_enumeration.addEnumeration(unicode_value='Gene Regulation Study', tag='Gene_Regulation_Study')
STD_ANON.Cancer_Genomics = STD_ANON._CF_enumeration.addEnumeration(unicode_value='Cancer Genomics', tag='Cancer_Genomics')
STD_ANON.Population_Genomics = STD_ANON._CF_enumeration.addEnumeration(unicode_value='Population Genomics', tag='Population_Genomics')
STD_ANON.RNASeq = STD_ANON._CF_enumeration.addEnumeration(unicode_value='RNASeq', tag='RNASeq')
STD_ANON.Exome_Sequencing = STD_ANON._CF_enumeration.addEnumeration(unicode_value='Exome Sequencing', tag='Exome_Sequencing')
STD_ANON.Pooled_Clone_Sequencing = STD_ANON._CF_enumeration.addEnumeration(unicode_value='Pooled Clone Sequencing', tag='Pooled_Clone_Sequencing')
STD_ANON.Transcriptome_Sequencing = STD_ANON._CF_enumeration.addEnumeration(unicode_value='Transcriptome Sequencing', tag='Transcriptome_Sequencing')
STD_ANON.Other = STD_ANON._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
STD_ANON._InitializeFacetMap(STD_ANON._CF_enumeration)
_module_typeBindings.STD_ANON = STD_ANON

# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.study.xsd', 30, 12)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element STUDY_TITLE uses Python identifier STUDY_TITLE
    __STUDY_TITLE = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'STUDY_TITLE'), 'STUDY_TITLE', '__AbsentNamespace0_CTD_ANON_STUDY_TITLE', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.study.xsd', 32, 16), )

    
    STUDY_TITLE = property(__STUDY_TITLE.value, __STUDY_TITLE.set, None, '\n                        Title of the study as would be used in a publication.\n                    ')

    
    # Element STUDY_TYPE uses Python identifier STUDY_TYPE
    __STUDY_TYPE = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'STUDY_TYPE'), 'STUDY_TYPE', '__AbsentNamespace0_CTD_ANON_STUDY_TYPE', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.study.xsd', 39, 16), )

    
    STUDY_TYPE = property(__STUDY_TYPE.value, __STUDY_TYPE.set, None, 'The STUDY_TYPE presents a controlled vocabulary for expressing the overall purpose of the study.')

    
    # Element STUDY_ABSTRACT uses Python identifier STUDY_ABSTRACT
    __STUDY_ABSTRACT = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'STUDY_ABSTRACT'), 'STUDY_ABSTRACT', '__AbsentNamespace0_CTD_ANON_STUDY_ABSTRACT', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.study.xsd', 163, 16), )

    
    STUDY_ABSTRACT = property(__STUDY_ABSTRACT.value, __STUDY_ABSTRACT.set, None, '\n                        Briefly describes the goals, purpose, and scope of the Study.  This need not be listed if it can be\n                        inherited from a referenced publication.\n                    ')

    
    # Element CENTER_NAME uses Python identifier CENTER_NAME
    __CENTER_NAME = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'CENTER_NAME'), 'CENTER_NAME', '__AbsentNamespace0_CTD_ANON_CENTER_NAME', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.study.xsd', 171, 16), )

    
    CENTER_NAME = property(__CENTER_NAME.value, __CENTER_NAME.set, None, '\n                        DEPRECATED.  Use STUDY@center_name instead.\n                        Controlled vocabulary identifying the sequencing center, core facility, consortium, or laboratory responsible for the study.\n                    ')

    
    # Element CENTER_PROJECT_NAME uses Python identifier CENTER_PROJECT_NAME
    __CENTER_PROJECT_NAME = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'CENTER_PROJECT_NAME'), 'CENTER_PROJECT_NAME', '__AbsentNamespace0_CTD_ANON_CENTER_PROJECT_NAME', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.study.xsd', 179, 16), )

    
    CENTER_PROJECT_NAME = property(__CENTER_PROJECT_NAME.value, __CENTER_PROJECT_NAME.set, None, "\n                        Submitter defined project name.  This field is intended for backward tracking of the study record to the submitter's LIMS.\n                    ")

    
    # Element PROJECT_ID uses Python identifier PROJECT_ID
    __PROJECT_ID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'PROJECT_ID'), 'PROJECT_ID', '__AbsentNamespace0_CTD_ANON_PROJECT_ID', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.study.xsd', 187, 16), )

    
    PROJECT_ID = property(__PROJECT_ID.value, __PROJECT_ID.set, None, '\n                        DEPRECATED (use RELATED_STUDIES.STUDY instead).  \n                        The required PROJECT_ID accession is generated by the Genome Project database at NCBI \n                        and will be valid also at the other archival institutions.  \n                    ')

    
    # Element RELATED_STUDIES uses Python identifier RELATED_STUDIES
    __RELATED_STUDIES = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'RELATED_STUDIES'), 'RELATED_STUDIES', '__AbsentNamespace0_CTD_ANON_RELATED_STUDIES', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.study.xsd', 197, 16), )

    
    RELATED_STUDIES = property(__RELATED_STUDIES.value, __RELATED_STUDIES.set, None, None)

    
    # Element STUDY_DESCRIPTION uses Python identifier STUDY_DESCRIPTION
    __STUDY_DESCRIPTION = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'STUDY_DESCRIPTION'), 'STUDY_DESCRIPTION', '__AbsentNamespace0_CTD_ANON_STUDY_DESCRIPTION', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.study.xsd', 230, 16), )

    
    STUDY_DESCRIPTION = property(__STUDY_DESCRIPTION.value, __STUDY_DESCRIPTION.set, None, '\n                        More extensive free-form description of the study.\n                    ')

    _ElementMap.update({
        __STUDY_TITLE.name() : __STUDY_TITLE,
        __STUDY_TYPE.name() : __STUDY_TYPE,
        __STUDY_ABSTRACT.name() : __STUDY_ABSTRACT,
        __CENTER_NAME.name() : __CENTER_NAME,
        __CENTER_PROJECT_NAME.name() : __CENTER_PROJECT_NAME,
        __PROJECT_ID.name() : __PROJECT_ID,
        __RELATED_STUDIES.name() : __RELATED_STUDIES,
        __STUDY_DESCRIPTION.name() : __STUDY_DESCRIPTION
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
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.study.xsd', 198, 18)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element RELATED_STUDY uses Python identifier RELATED_STUDY
    __RELATED_STUDY = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'RELATED_STUDY'), 'RELATED_STUDY', '__AbsentNamespace0_CTD_ANON__RELATED_STUDY', True, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.study.xsd', 200, 22), )

    
    RELATED_STUDY = property(__RELATED_STUDY.value, __RELATED_STUDY.set, None, None)

    _ElementMap.update({
        __RELATED_STUDY.name() : __RELATED_STUDY
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
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.study.xsd', 201, 24)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element RELATED_LINK uses Python identifier RELATED_LINK
    __RELATED_LINK = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'RELATED_LINK'), 'RELATED_LINK', '__AbsentNamespace0_CTD_ANON_2_RELATED_LINK', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.study.xsd', 203, 28), )

    
    RELATED_LINK = property(__RELATED_LINK.value, __RELATED_LINK.set, None, "\n                                Related study or project record from a list of supported databases.\n                                The study's information is derived from this project record rather\n                                than stored as first class information.\n                              ")

    
    # Element IS_PRIMARY uses Python identifier IS_PRIMARY
    __IS_PRIMARY = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'IS_PRIMARY'), 'IS_PRIMARY', '__AbsentNamespace0_CTD_ANON_2_IS_PRIMARY', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.study.xsd', 213, 28), )

    
    IS_PRIMARY = property(__IS_PRIMARY.value, __IS_PRIMARY.set, None, '\n                                Whether this study object is designated as the primary source\n                                of the study or project information.\n                              ')

    _ElementMap.update({
        __RELATED_LINK.name() : __RELATED_LINK,
        __IS_PRIMARY.name() : __IS_PRIMARY
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_2 = CTD_ANON_2


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    """
                  Links to resources related to this study (publication, datasets, online databases).
              """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.study.xsd', 247, 12)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element STUDY_LINK uses Python identifier STUDY_LINK
    __STUDY_LINK = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'STUDY_LINK'), 'STUDY_LINK', '__AbsentNamespace0_CTD_ANON_3_STUDY_LINK', True, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.study.xsd', 249, 16), )

    
    STUDY_LINK = property(__STUDY_LINK.value, __STUDY_LINK.set, None, None)

    _ElementMap.update({
        __STUDY_LINK.name() : __STUDY_LINK
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_3 = CTD_ANON_3


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_4 (pyxb.binding.basis.complexTypeDefinition):
    """
               Properties and attributes of the study.  These can be entered as free-form 
               tag-value pairs. For certain studies, submitters may be asked to follow a
               community established ontology when describing the work.
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.study.xsd', 262, 12)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element STUDY_ATTRIBUTE uses Python identifier STUDY_ATTRIBUTE
    __STUDY_ATTRIBUTE = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'STUDY_ATTRIBUTE'), 'STUDY_ATTRIBUTE', '__AbsentNamespace0_CTD_ANON_4_STUDY_ATTRIBUTE', True, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.study.xsd', 264, 16), )

    
    STUDY_ATTRIBUTE = property(__STUDY_ATTRIBUTE.value, __STUDY_ATTRIBUTE.set, None, None)

    _ElementMap.update({
        __STUDY_ATTRIBUTE.name() : __STUDY_ATTRIBUTE
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_4 = CTD_ANON_4


# Complex type StudySetType with content type ELEMENT_ONLY
class StudySetType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type StudySetType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'StudySetType')
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.study.xsd', 273, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element STUDY uses Python identifier STUDY
    __STUDY = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'STUDY'), 'STUDY', '__AbsentNamespace0_StudySetType_STUDY', True, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.study.xsd', 275, 6), )

    
    STUDY = property(__STUDY.value, __STUDY.set, None, None)

    _ElementMap.update({
        __STUDY.name() : __STUDY
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.StudySetType = StudySetType
Namespace.addCategoryObject('typeBinding', 'StudySetType', StudySetType)


# Complex type StudyType with content type ELEMENT_ONLY
class StudyType (_ImportedBinding__com.ObjectType):
    """
          A Study is a container for a sequencing investigation that may comprise multiple experiments.
          The Study has an overall goal, but is otherwise minimally defined in the SRA. 
          A Study is composed of a descriptor, zero or more experiments, and zero or more analyses.
          The submitter may decorate the Study with web links and properties.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'StudyType')
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.study.xsd', 17, 2)
    _ElementMap = _ImportedBinding__com.ObjectType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__com.ObjectType._AttributeMap.copy()
    # Base type is _ImportedBinding__com.ObjectType
    
    # Element DESCRIPTOR uses Python identifier DESCRIPTOR
    __DESCRIPTOR = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'DESCRIPTOR'), 'DESCRIPTOR', '__AbsentNamespace0_StudyType_DESCRIPTOR', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.study.xsd', 29, 10), )

    
    DESCRIPTOR = property(__DESCRIPTOR.value, __DESCRIPTOR.set, None, None)

    
    # Element STUDY_LINKS uses Python identifier STUDY_LINKS
    __STUDY_LINKS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'STUDY_LINKS'), 'STUDY_LINKS', '__AbsentNamespace0_StudyType_STUDY_LINKS', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.study.xsd', 241, 10), )

    
    STUDY_LINKS = property(__STUDY_LINKS.value, __STUDY_LINKS.set, None, '\n                  Links to resources related to this study (publication, datasets, online databases).\n              ')

    
    # Element STUDY_ATTRIBUTES uses Python identifier STUDY_ATTRIBUTES
    __STUDY_ATTRIBUTES = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'STUDY_ATTRIBUTES'), 'STUDY_ATTRIBUTES', '__AbsentNamespace0_StudyType_STUDY_ATTRIBUTES', False, pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.study.xsd', 254, 10), )

    
    STUDY_ATTRIBUTES = property(__STUDY_ATTRIBUTES.value, __STUDY_ATTRIBUTES.set, None, '\n               Properties and attributes of the study.  These can be entered as free-form \n               tag-value pairs. For certain studies, submitters may be asked to follow a\n               community established ontology when describing the work.\n            ')

    
    # Element IDENTIFIERS (IDENTIFIERS) inherited from {SRA.common}ObjectType
    
    # Attribute alias inherited from {SRA.common}ObjectType
    
    # Attribute center_name inherited from {SRA.common}ObjectType
    
    # Attribute broker_name inherited from {SRA.common}ObjectType
    
    # Attribute accession inherited from {SRA.common}ObjectType
    _ElementMap.update({
        __DESCRIPTOR.name() : __DESCRIPTOR,
        __STUDY_LINKS.name() : __STUDY_LINKS,
        __STUDY_ATTRIBUTES.name() : __STUDY_ATTRIBUTES
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.StudyType = StudyType
Namespace.addCategoryObject('typeBinding', 'StudyType', StudyType)


# Complex type [anonymous] with content type EMPTY
class CTD_ANON_5 (pyxb.binding.basis.complexTypeDefinition):
    """The STUDY_TYPE presents a controlled vocabulary for expressing the overall purpose of the study."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.study.xsd', 43, 18)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute existing_study_type uses Python identifier existing_study_type
    __existing_study_type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'existing_study_type'), 'existing_study_type', '__AbsentNamespace0_CTD_ANON_5_existing_study_type', _module_typeBindings.STD_ANON, required=True)
    __existing_study_type._DeclarationLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.study.xsd', 44, 20)
    __existing_study_type._UseLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.study.xsd', 44, 20)
    
    existing_study_type = property(__existing_study_type.value, __existing_study_type.set, None, None)

    
    # Attribute new_study_type uses Python identifier new_study_type
    __new_study_type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'new_study_type'), 'new_study_type', '__AbsentNamespace0_CTD_ANON_5_new_study_type', pyxb.binding.datatypes.string)
    __new_study_type._DeclarationLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.study.xsd', 154, 20)
    __new_study_type._UseLocation = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.study.xsd', 154, 20)
    
    new_study_type = property(__new_study_type.value, __new_study_type.set, None, '\n                      To propose a new term, select Other and enter a new study type.\n                    ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __existing_study_type.name() : __existing_study_type,
        __new_study_type.name() : __new_study_type
    })
_module_typeBindings.CTD_ANON_5 = CTD_ANON_5


STUDY_SET = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'STUDY_SET'), StudySetType, documentation='\n      An STUDY_SET is a container for a set of studies and a common namespace.\n    ', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.study.xsd', 279, 2))
Namespace.addCategoryObject('elementBinding', STUDY_SET.name().localName(), STUDY_SET)

STUDY = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'STUDY'), StudyType, location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.study.xsd', 288, 2))
Namespace.addCategoryObject('elementBinding', STUDY.name().localName(), STUDY)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'STUDY_TITLE'), pyxb.binding.datatypes.string, scope=CTD_ANON, documentation='\n                        Title of the study as would be used in a publication.\n                    ', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.study.xsd', 32, 16)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'STUDY_TYPE'), CTD_ANON_5, scope=CTD_ANON, documentation='The STUDY_TYPE presents a controlled vocabulary for expressing the overall purpose of the study.', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.study.xsd', 39, 16)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'STUDY_ABSTRACT'), pyxb.binding.datatypes.string, scope=CTD_ANON, documentation='\n                        Briefly describes the goals, purpose, and scope of the Study.  This need not be listed if it can be\n                        inherited from a referenced publication.\n                    ', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.study.xsd', 163, 16)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'CENTER_NAME'), pyxb.binding.datatypes.string, scope=CTD_ANON, documentation='\n                        DEPRECATED.  Use STUDY@center_name instead.\n                        Controlled vocabulary identifying the sequencing center, core facility, consortium, or laboratory responsible for the study.\n                    ', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.study.xsd', 171, 16)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'CENTER_PROJECT_NAME'), pyxb.binding.datatypes.string, scope=CTD_ANON, documentation="\n                        Submitter defined project name.  This field is intended for backward tracking of the study record to the submitter's LIMS.\n                    ", location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.study.xsd', 179, 16)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'PROJECT_ID'), pyxb.binding.datatypes.nonNegativeInteger, scope=CTD_ANON, documentation='\n                        DEPRECATED (use RELATED_STUDIES.STUDY instead).  \n                        The required PROJECT_ID accession is generated by the Genome Project database at NCBI \n                        and will be valid also at the other archival institutions.  \n                    ', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.study.xsd', 187, 16)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'RELATED_STUDIES'), CTD_ANON_, scope=CTD_ANON, location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.study.xsd', 197, 16)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'STUDY_DESCRIPTION'), pyxb.binding.datatypes.string, scope=CTD_ANON, documentation='\n                        More extensive free-form description of the study.\n                    ', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.study.xsd', 230, 16)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'STUDY_TITLE')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.study.xsd', 32, 16))
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
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'STUDY_TYPE')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.study.xsd', 39, 16))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.study.xsd', 163, 16))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'STUDY_ABSTRACT')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.study.xsd', 163, 16))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.study.xsd', 171, 16))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'CENTER_NAME')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.study.xsd', 171, 16))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.study.xsd', 179, 16))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'CENTER_PROJECT_NAME')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.study.xsd', 179, 16))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.study.xsd', 187, 16))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'PROJECT_ID')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.study.xsd', 187, 16))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.study.xsd', 197, 16))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'RELATED_STUDIES')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.study.xsd', 197, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.study.xsd', 230, 16))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'STUDY_DESCRIPTION')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.study.xsd', 230, 16))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.study.xsd', 31, 14))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.study.xsd', 163, 16))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.study.xsd', 171, 16))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.study.xsd', 179, 16))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.study.xsd', 187, 16))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.study.xsd', 197, 16))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.study.xsd', 230, 16))
    counters.add(cc_6)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_())
    sub_automata.append(_BuildAutomaton_2())
    sub_automata.append(_BuildAutomaton_3())
    sub_automata.append(_BuildAutomaton_4())
    sub_automata.append(_BuildAutomaton_5())
    sub_automata.append(_BuildAutomaton_6())
    sub_automata.append(_BuildAutomaton_7())
    sub_automata.append(_BuildAutomaton_8())
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.study.xsd', 31, 14)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'RELATED_STUDY'), CTD_ANON_2, scope=CTD_ANON_, location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.study.xsd', 200, 22)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, 'RELATED_STUDY')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.study.xsd', 200, 22))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_9()




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'RELATED_LINK'), _ImportedBinding__com.XRefType, scope=CTD_ANON_2, documentation="\n                                Related study or project record from a list of supported databases.\n                                The study's information is derived from this project record rather\n                                than stored as first class information.\n                              ", location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.study.xsd', 203, 28)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'IS_PRIMARY'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_2, documentation='\n                                Whether this study object is designated as the primary source\n                                of the study or project information.\n                              ', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.study.xsd', 213, 28)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(None, 'RELATED_LINK')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.study.xsd', 203, 28))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(None, 'IS_PRIMARY')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.study.xsd', 213, 28))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_2._Automaton = _BuildAutomaton_10()




CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'STUDY_LINK'), _ImportedBinding__com.LinkType, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.study.xsd', 249, 16)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(None, 'STUDY_LINK')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.study.xsd', 249, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_3._Automaton = _BuildAutomaton_11()




CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'STUDY_ATTRIBUTE'), _ImportedBinding__com.AttributeType, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.study.xsd', 264, 16)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(None, 'STUDY_ATTRIBUTE')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.study.xsd', 264, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_4._Automaton = _BuildAutomaton_12()




StudySetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'STUDY'), StudyType, scope=StudySetType, location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.study.xsd', 275, 6)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(StudySetType._UseForTag(pyxb.namespace.ExpandedName(None, 'STUDY')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.study.xsd', 275, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
StudySetType._Automaton = _BuildAutomaton_13()




StudyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'DESCRIPTOR'), CTD_ANON, scope=StudyType, location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.study.xsd', 29, 10)))

StudyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'STUDY_LINKS'), CTD_ANON_3, scope=StudyType, documentation='\n                  Links to resources related to this study (publication, datasets, online databases).\n              ', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.study.xsd', 241, 10)))

StudyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'STUDY_ATTRIBUTES'), CTD_ANON_4, scope=StudyType, documentation='\n               Properties and attributes of the study.  These can be entered as free-form \n               tag-value pairs. For certain studies, submitters may be asked to follow a\n               community established ontology when describing the work.\n            ', location=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.study.xsd', 254, 10)))

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 19, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.study.xsd', 241, 10))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.study.xsd', 254, 10))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(StudyType._UseForTag(pyxb.namespace.ExpandedName(None, 'IDENTIFIERS')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.common.xsd', 19, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(StudyType._UseForTag(pyxb.namespace.ExpandedName(None, 'DESCRIPTOR')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.study.xsd', 29, 10))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(StudyType._UseForTag(pyxb.namespace.ExpandedName(None, 'STUDY_LINKS')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.study.xsd', 241, 10))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(StudyType._UseForTag(pyxb.namespace.ExpandedName(None, 'STUDY_ATTRIBUTES')), pyxb.utils.utility.Location('ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.study.xsd', 254, 10))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
StudyType._Automaton = _BuildAutomaton_14()

