<h2>An API about 21st Century greatest novels as described on BBC site by Jane Ciabattari on 19 January 2015.</h2>
<p>URL</p>
<ul>
<li>/api/books/all</li>
<li>/api/books/id?  - Required id=[integer] </li>
<li>/api/books/author? - Required author=[string] </li>
<li>/api/books/title? - Required title=[string] </li>
<li>/api/books/all? – Required year=[string] </li>
</ul>
<p>METHOD</p>
<ul><li>Get</li></ul>
<p>Success Response:</p>
<pre>Content:
[
  {
    "author": "Michael Chabon", 
    "id": 6, 
    "published": "2000", 
    "title": "The Amazing Adventures of Kavalier & Clay"
  }
]
</pre>
<p>Error Response:</p>
<pre>[]</pre>
<p>Or</p>
<pre>Not Found</pre>
</pre>
