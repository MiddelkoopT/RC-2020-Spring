# Top500 Metadata

> https://www.top500.org/project/top500_description/ (2020-03-16)

## TOP500 DESCRIPTION

The TOP500 table shows the 500 most powerful commercially available
computer systems known to us. To keep the list as compact as possible,
we show only a part of our information here:

* Nworld - Position within the TOP500 ranking
* Manufacturer - Manufacturer or vendor
* Computer - Type indicated by manufacturer or vendor
* Installation Site - Customer
* Location - Location and country
* Year - Year of installation/last major update
* Field of Application
* #Proc. - Number of processors (Cores)
* Rmax - Maximal LINPACK performance achieved
* Rpeak - Theoretical peak performance
* Nmax - Problem size for achieving Rmax
* N1/2 - Problem size for achieving half of Rmax

If Rmax from Table 3 of the LINPACK Report is not available, we use
the TPP performance given in Table 1 of the LINPACK Report for solving
a system of 1000 equations. In a few cases we interpolated between two
measured system sizes or we scaled by cycle times. For models where we
did not receive the requested data, the performance of the next
smaller system measured is used.

If there should be any changes in the performances given in the
following table we will update them.

In addition to cross checking different sources of information, we
select randomly a statistical representative sample of the first 500
systems of our database. For these systems we ask the supplier of the
information to establish direct contact between the installation site
and us to verify the given information. This gives us basic
information about the quality of the list in total.

As the TOP500 should provide a basis for statistics on the market of
high-performance computers, we limit the number of systems installed
at vendor sites. This is done for each vendor separately by limiting
the accumulated performance of systems at vendor sites to a maximum of
5% of the total accumulated installed performance of this
vendor. Rounding is done in favor of the vendor in question.

In the TOP500 List table, the computers are ordered first by their
Rmax value. In the case of equal performances (Rmax value) for
different computers, we have chosen to order by Rpeak. For sites that
have the same computer, the order is by memory size and then
alphabetically.
