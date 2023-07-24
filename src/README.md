# Charter
-------------
## Objectives and project purpose
-------------
### Objective

Active participation of Danngn Market users in trading.
- In various regions of Korea, many users are using the Dangn Market app to trade second-hand.
- But many people have a hard time deciding which of my used products to sell. 
- Because they doubt who will buy the things they use.
- Also, there are many people who want to buy what they want outside the scope of certification of Dangn Market.
- We will provide data on which item categories people in the area are most interested in through data.
- Such a service can induce users to participate in a transaction with their used goods, and can also increase the participation rate of those who are far away.

-------------
## Project scope

###  Collect
I will crawl the data from Daangn Market website by using Python.
The names of modules are requests and BeautifulSoup of bs4.

-------------

### Process
All files imported through crawling are saved as CSV file and JSON file.
Especially I made some modules for this project. So it doesn't need to import other special packages.

-------------

### Store
CSV and JSON files are sent to and stored in databases of SQLite and Elasticsearch.

-  JSON schema description for NoSQL
```
All_Data
{
  local_name: text,
  Item : text,
  Like : number,
  Chat : number,
  Date : date
}
```

```
Local_Data
{
  local_name: text,
  Item_name : text,
  Like : number,
  Chat : number,
  Date : date
}
```

<table>
  <tr>
    <td colspan="1">
      Column Family Name
    </td>
    <td colspan="2">
      local_name
    </td>
  </tr>
  <tr>
    <td colspan="1" rowspan="3">
      All_Data
    </td>
  </tr>
  <tr>
    <td>
        Item
    </td>
    <td>
        Chat
    </td>
  </tr>
  <tr>
    <td>
        Count
    </td>
    <td>
        Like
    </td>
  </tr>
  <tr>
  </tr>
  <tr>
    <td colspan="1" rowspan="4">
      Local_Data
    </td>
  </tr>
  <tr>
    <td>
        Item_name
    </td>
    <td>
        Chat
    </td>
  </tr>
  <tr>
    <td>
        Like
    </td>
    <td>
        Date
    </td>
  </tr>
    </td>
  </tr>
</table>

--------
## Query
After data is properly stored in the database, all data are accessed and processed through query statements.

