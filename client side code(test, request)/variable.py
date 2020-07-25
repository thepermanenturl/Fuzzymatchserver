true=True
false=False
d={
"train_fields": [{
"header": "Content id",
"required": true,
"description": "The id of your data",
"fuzzy_suggestions": ["id", "pk"],
"example_values": ["123", "123_xyz"]
},
{
"header": "label",
"required": true,
"description": "The label of your data",
"fuzzy_suggestions": ["title", "name"],
"example_values": ["This is a title", "This is a title again"]
}
],
"test_fields": [{
"header": "id",
"sample values": ["123", "1234", "345"]
},
{
"header": "name",
"sample values": ["This is a name", "This is a title", "This is a name again"]
},
{
"header": "dummy",
"sample values": ["This is a bluff", "This is a dummy", "This is bogus"]
}
]
}