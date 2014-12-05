Storing Direct Addresses in NPPES:
=================================

_Last Updated: December 5, 2014_

This document outlines how direct addresses are stored in the NPPES prototype, currently and outlines other approaches. These have been updated and expanded to five options based on Google Group comments.


Background
----------

Direct addresses are stored in the provider document in an array `[]`,
called `direct_addresses` where there can be 0..n addresses.  `is_public` 
is the switch to make the address public in the data_dissemination / API.
This defaults to `true`. The first table outlines the data model now, and the following tow tables offer some other options.



Direct Addresses - Current Option 1 (Loose)
-------------------------------------------

<table>
<tr>
  <td>Name</td>
  <td>Max Length</td>
  <td>Required</td>
  <td>Notes</td>
</tr>

<tr>
  <td>email</td>
  <td>150</td>
  <td>Y</td>
  <td>A Direct address</td>
</tr>

<tr>
  <td>organization</td>
  <td>150</td>
  <td>Y</td>
  <td>Name of organization</td>
</tr>

<tr>
  <td>is_public</td>
  <td>Boolean</td>
  <td>Y</td>
  <td>`true` if Direct address is public and `false` otherwise.</td>
</tr>

</table>

Valid Example:

    {
    "email"         : "jtkirk@direct.example.com",
    "organization"  : "Enterprise Health",
    "is_pubic"      : true,
    }


in must be registered in an NPI-2 record.

Direct Addresses Option #2 (Hybrid)
-------------------------------------

<table>
<tr>
  <td>Name</td>
  <td>Max Length</td>
  <td>Required</td>
  <td>Notes</td>
</tr>

<tr>
  <td>email</td>
  <td>150</td>
  <td>Y</td>
  <td>A Direct address</td>
</tr>

<tr>
  <td>organization</td>
  <td>150</td>
  <td>S</td>
  <td>Name of organization if organization identifier not provided.
  If `organization_npi` is given this value must match the NPI-2's,
  `organization_name`.
  </td>
</tr>

<tr>
  <td>organization_npi_2</td>
  <td>10</td>
  <td>S</td>
  <td>Required if organization name not provided.  If given, the NPI-2 must exist, and be an active organization (NPI-2). If `organization_name` is blank, it may be auto-populated with NPI-2's `oreganization_name` by NPPES.</td>
</tr>

<tr>
  <td>is_public</td>
  <td>Boolean</td>
  <td>Y</td>
  <td>`true` if Direct address is public and `false` otherwise.</td>
</tr>

</table>


Valid Example 1:


    {
    "email"              : "jtkirk@direct.example.com",
    "organization_name"  : "Enterprise Health",
    "is_pubic"           : true,
    }


Valid Example 2:


    {
    "email"               : "jtkirk@direct.example.com",
    "organization_npi"    : 1234567890,
    "is_pubic"            : false,
    }

Invalid Example 1:

    {
    "email"               : "jtkirk@direct.example.com",
    "organization_npi"    : 1234567890,
    "organization_name"   : "Klingon Health",
    "is_pubic"            : true,
    }

In the above example we assume the organization_npi_1's organization_name
does not match.



Direct Addresses Option #3 (Strict)
-----------------------------------

<table>
<tr>
  <td>Name</td>
  <td>Max Length</td>
  <td>Required</td>
  <td>Notes</td>
</tr>

<tr>
  <td>email</td>
  <td>150</td>
  <td>Y</td>
  <td>A Direct address</td>
</tr>

<tr>
  <td>organization_name</td>
  <td>150</td>
  <td>N</td>
  <td>This value is system generated and ignored if submitted.
  </td>
</tr>

<tr>
  <td>organization_npi</td>
  <td>10</td>
  <td>Y</td>
  <td>Required if organization name not provided.</td>
</tr>

<tr>
  <td>is_public</td>
  <td>Boolean</td>
  <td>Y</td>
  <td>`true` if Direct address is public and `false` otherwise.</td>
</tr>

</table>


Valid Example 1:


    {
    "email"               : "jtkirk@direct.example.com",
    "organization_npi_2"  : 1234567890,
    "is_pubic"            : false,
    }

Invalid Example 1:


    {
    "email"               : "jtkirk@direct.example.com",
    "organization_name"   : "Enterprise Health",
    "is_pubic"            : true,
    }




Direct Addresses Option #4 (More Strict)
-----------------------------------

Organizational domains may be added to the NPI-2 Record in the
`direct_domains` array.  `direct_domain` object is defined below:


direct_domain
--------------
<table>
<tr>
  <td>Name</td>
  <td>Max Length</td>
  <td>Required</td>
  <td>Notes</td>
</tr>

<tr>
  <td>domain</td>
  <td>150</td>
  <td>Y</td>
  <td>A direct domain controled by this NPI. Organizations may have 0..N domains defined. No two NPI-2 records may share the same domain,</td>
</tr>




</table>

direct_address
--------------

<table>

<tr>
  <td>email</td>
  <td>150</td>
  <td>Y</td>
  <td>A Direct address.</td>
</tr>


<tr>
  <td>organization_npi</td>
  <td>10</td>
  <td>Y</td>
  <td>Required if `is_organization` = `true`. The `NPI-2` must exist and be active ('statu's = 'A')</td>
</tr>

<tr>
  <td>is_organization</td>
  <td>Boolean</td>
  <td>N</td>
  <td>Required if organization name not provided. Warning if domain not registered in an NPI-2 record.</td>
</tr>


</table>


Valid Example 1:
     #Domain in NPI-1 or sole proprietor only
    {
    "domain"               : "direct.example.com",
    "organization_npi      : 1234567891,

    }
    #Email in NPI-1 or NPI-2
    {
    "email"               : "jtkirk@direct.example.com",
    "organization_npi      : 1234567890,
    }



Direct Addresses Option #5 (Most Strict)
-----------------------------------------

Organizational domains may be added to the NPI-2 Record in the
`direct_domains` array.  `direct_domain` object is defined below:


direct_domain
--------------
<table>
<tr>
  <td>Name</td>
  <td>Max Length</td>
  <td>Required</td>
  <td>Notes</td>
</tr>

<tr>
  <td>domain</td>
  <td>150</td>
  <td>Y</td>
  <td>A direct domain controled by this NPI. Organizations may have 0..N domains defined. No two NPI-2 records may share the same domain,</td>
</tr>

</table>

direct_address
--------------

<table>

<tr>
  <td>email</td>
  <td>150</td>
  <td>Y</td>
  <td>A Direct address. The address must be discoverable via DNS or LDAP.</td>
</tr>


<tr>
  <td>organization_npi</td>
  <td>10</td>
  <td>Y</td>
  <td>Required if organization name not provided. Domain must be registered in an NPI-2 record.</td>
</tr>

</table>


Valid Example 1:
     #Domain in NPI-1 or sole proprietor only
    {
    "domain"               : "direct.example.com",
    "organization_npi      : 1234567891,

    }
    #Email in NPI-1 or NPI-2
    {
    "email"               : "jtkirk@direct.example.com",
    "organization_npi      : 1234567890,
    }
