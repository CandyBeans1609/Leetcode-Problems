select Person.firstname as firstName,Person.lastname as lastName ,Address.city as city,Address.state as state
from Person
left join Address
on Person.personId=Address.personId
