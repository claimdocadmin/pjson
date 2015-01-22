Representing Associations Between Actors in the US Healthcare Ecosystem
=======================================================================


The document is a draft proposed format for implementing "associations" 
between the various actors in the US health care ecosystem. This includes 
entity to entity relationships as well as endpoints (including Direct 
addresses and URLs). It is based on the Provider JSON enumeration object 
format(<https://github.com/HHSIDEAlab/pjson>).  `associations` is an 
arrary (i.e. a list of 0..N) `[]` of objects `{}` 
(i.e. a dictionary or hash) attached to the top level of our 
enumeration object `{}`.  For example:

    {
        "enumeration_type": "NPI-2",
        "number": "12345678901",
        .
        .
        "associations" : [ {association1}, {association2},...]

	}



Introduction
============

Associations store relationships between entities as well as health information exchange endpoints.  Often these can be combined into one assication. For example, we can say that "Dr. Sally with NPI-1 of 1111111111 is part of XYZ, Hospital(with an NPI-2 of 1234567890) and has a Direct address of sally@xyzdirect.example.com and is not accepting new patients here".

Simple Organization Example (within an NPI-2 document):

    {
    "enumeration_type": "NPI-2",
    "number": "1234567890",
     .
     .
     "associations" : [ 
     			    {
     				"purpose_type":            "PROVIDER-NETWORK",
     				"association_data_type":   "NPI-1",
     				"association_identifier":  "1111111111",
     				"endpoint_data_type":      "DIRECT-EMAIL-ADDRESS",
     				"endpoint":                "sally@xyzdirect.example.com"
					}
     	]
	}

Simple Individual Example (within an NPI-1 document):

    {
    "enumeration_type": "NPI-1",
    "number": "1111111111",
     .
     .
     "associations" : [ 
     			    {
     				"purpose_type":            "PROVIDER-NETWORK",
     				"association_data_type":   "NPI-2",
     				"association_identifier":  "1234567890",
     				"endpoint_data_type":      "DIRECT-EMAIL-ADDRESS",
     				"endpoint":                "sally@xyzdirect.example.com"
					}
     	]
	}


Detailed Specification
======================


Associations contain several codified types (i.e. metadata) that classify the data and laregly control what is required versus what is optional. These codified types are `purpose`,  `association_data_type`, and `endpoint_data_type`.  `purpose` is always required, while `association_data_type`, and `endpoint_data_type` are sometimes required based on the specific `purpose`.

<table>

<tr>
  <td>Name</td>
  <td>Max Length</td>
  <td>Required</td>
  <td>Notes</td>
</tr>

<tr>
  <td>purpose</td>
  <td>50</td>
  <td>Y</td>
  <td>
  The `purpose` determines a number of other requirements for the object.
  Must be in  [ `HIE-EXCHANGE`,
                  `MEDICARE-NETWORK`, `MEDICAID-NETWORK`, `PRIVATE-PAYER-NETWORK`,
                  `ACO-NETWORK`, `PROVIDER-NETWORK`,
                  `DOMAIN`, `PARENT-ORGANIZATION`] </td>
</tr>


<tr>
  <td>association_data_type</td>
  <td>6</td>
  <td>S</td>
  <td>
   Must be in
   [`NPI-1`, `NPI-2`, `HPID`, `OEID`, `MAC`, `EIN`, `PAC-ID`, `OTHER`].
   Required when `purpose` in [`HIE-EXCHANGE`, `MEDICARE-NETWORK`, `PRIVATE-PAYER-NETWORK`,
   `ACO-NETWORK`, `PROVIDER-NETWORK`,`PARENT-ORGANIZATION`]
  </td>
</tr>



<tr>
  <td>endpoint_data_type</td>
  <td>50</td>
  <td>S</td>
  <td>
   Required when purpose=`HIE-EXCHANGE`.
   Must be in 
   [`DIRECT-EMAIL-ADDRESS`,
   `REGULAR-EMAIL-ADDRESS`,
   `SOAP-WS-URL`,
   `CONNECT-URL`,
   `FHIR-URL`,
   `RESTFUL-WS-URL`,
   `WEBSITE-URL`,
   `OTHER-URL`]
  </td>
</tr>


<tr>
  <td>association_identifier</td>
  <td>1024</td>
  <td>S</td>
  <td>
 The association's identifier. Required if `association_data_type` is in [`NPI-1`,`NPI-2`,`HPID`, `OEID`, `MAC`, `EIN` ] or if `purpose` is in [`HIE-EXCHANGE`,`MEDICAID-NETWORK`, `PAYER-NETWORK`, `ACO-NETWORK`, `DOMAIN`, `MEDICARE-NETWORK`, `PROVIDES-SERVICES-ON-BEHALF-OF-THIS-ORG`, `PARENT-ORGANIZATION`]
  </td>
</tr>




<tr>
  <td>endpoint</td>
  <td>1024</td>
  <td>S</td>
  <td>Required when `purpose` is `HIE-EXCHANGE`, or `DOMAIN`. </td>
</tr>


<tr>
  <td>accepting_new_patients</td>
  <td>Boolean</td>
  <td>N</td>
  <td>`true` or `false`.</td>
</tr>


<tr>
  <td>description</td>
  <td>1024</td>
  <td>N</td>
  <td>Description or written purpose of the association.</td>
</tr>


</table>


More Examples
=============


Direct Examples
----------------

A provider associated with an organization with a Direct address.

    {
     "purpose_type":            "HIE-EXCHANGE",
     "association_data_type":   "NPI-2",
     "association_identifier": 	"12334567890",
     "endpoint_data_type":      "DIRECT-EMAIL-ADDRESS",
     "endpoint":                "jtkirk@direct.example.com"

	}



A provider associated with an organization with a Direct address.

    {
     "purpose_type":            "HIE-EXCHANGE",
     "association_data_type":   "NPI-2",
     "assoication_identifier":  "12334567890",
     "endpoint_data_type":      "DIRECT-EMAIL-ADDRESS",
     "endpoint":                "jtkirk@direct.example.com",
	}



A MAC associated with an organization with a Direct address.

    {
     "purpose_type":            "HIE-EXCHANGE",
     "association_data_type":   "MAC",
     "association_identifier": 	"3",
     "endpoint_data_type":      "DIRECT-EMAIL-ADDRESS",
     "endpoint":                "jtkirk@direct.example.com"
	}




Adding a Direct Domain to an NPI-2.

    {
     "purpose_type":            "HIE-EXCHANGE",
     "association_data_type":   "NPI-2",
     "association_identifier":  "12334567890",
     "endpoint_data_type":      "DOMAIN",
     "endpoint":                "direct.example.com"
	}

Generic Association Examples
----------------------------


Provider-Payer Example 1: The provider is part of this health plan's network. This example is given in the context of an `HPID` document.


    {
    "enumeration_type": "HPID",
    "number": "7000000001",
    .
    .
    "associations": [

        {
        "purpose":                 "PAYER-NETWORK",
        "association_data_type":   "NPI-2",
        "association_identifier":  "1234567890"
        },
         .
         .
        ]

    }


Provider-Payer Example #2: The provider is part of this health plan's network. This example is given in the context of an `NPI-1` document.



    {
    "enumeration_type": "NPI-1",
    "number":           "1111111111",
    .
    .
    "associations": [

        {
        "purpose":                 "PAYER-NETWORK",
        "association_data_type":   "HPID",
        "association_identifier:   "7000000002",
        "accepting_new_patients":  true
        },
         .
         .
        ]
	}

Provider-Medicare Association

    {
    "enumeration_type": "NPI-2",
    "number": "1222222222",
    .
    .
    "associations": [

            {
            "purpose":                "MEDICARE-NETWORK",
            "association_data_type":  "PAC-ID",
            "association_identifier": "3456783456",
            "accepting_new_patients": true
            },
             .
             .
            ]
	}



Other Entity-ACO Association ( NPI-2 --> OEID Assumes an the ACI has an NPI-2)

    {
    "enumeration_type": "NPI-2",
    "number": "1222222222",
    .
    .
    "associations": [

            {
            "purpose":                "ACO-NETWORK",
            "association_data_type":  "OEID",
            "association_identifier": "6029384756"
            },
             .
             .
            ]
	}




Combination Examples
--------------------

Individual provider to Organization  (NPI-1 --> NPI-2) Association with a Direct address.




    {
    "enumeration_type": "NPI-2",
    "number": "1222222222",
    .
    .
    "associations": [

            {
            "purpose":                "PROVIDER-NETWORK",
            "association_data_type":  "NPI-2",
            "association_identifier": "1234543211",
            "endpoint_data_type":     "DIRECT-EMAIL-ADDRESS",
            "endpoint":               "jtkirk@direct.example.com"
            },
             .
             .
            ]
	}



Webservice, etc. Examples
-------------------------

A homepage URL in an individual provider's document




    {
    "enumeration_type": "NPI-1",
    "number": "1575938278",
    .
    .
    "associations": [

            {
            "purpose":                "OTHER",
            "endpoint_data_type":     "WEBSITE-URL",
            "endpoint":               "http://example.com"
            },
     		.
     		.
    		]
	}

Add a Connect URL to a Provider organization document


    {
    "enumeration_type": "NPI-2",
    "number": "1222222222",
    .
    .
    "associations": [

            {
            "purpose":                "HIE-EXCHANGE",
            "endpoint_data_type":     "CONNECT-URL",
            "endpoint":               "http://connect.example.com/connect.wsgi"
            },
             .
             .
            ]

	}




Add an arbitrary RESTFul service to a Provider organization document


    {
    "enumeration_type": "NPI-2",
    "number": "1222222222",
    .
    .
    "associations": [

            {
            "purpose":                "HIE-EXCHANGE",
            "endpoint_data_type":     "RESTFUL-WS-URL",
            "endpoint":               "https://example.com/some-service",
            "description":            "Fetches the lastest data on x,y,z"
            },
             .
             .
            ]

	}


Add a Healthcare Directory to a provider organization document


    {
    "enumeration_type": "NPI-2",
    "number": "1222222222",
    .
    .
    "associations": [

            {
            "purpose":                "HIE-EXCHANGE",
            "endpoint_data_type":     "HD-URL",
            "endpoint":               "https://hpdplus.example.com/hd.wsgi"
            },
             .
             .
            ]

	}





