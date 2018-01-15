import tempfile

mail_content = tempfile.NamedTemporaryFile(mode='w')
mail = """
<html>
<head>
  <style type="text/css">

  table.information td [
    font-family: "Open Sans", sans-serif;
    fint-size: 30px;
  ]

  table [
    border-collapse: collapse;
    border-top-color: rgb(221, 221, 221);
    border-top-style: solid;
    border-top-width: 1px;
    box-sizing: border-box;
    color: rgb(77, 77, 77);
    display: table-cell;
    float: none;
    font-family: "Open Sans", sans-serif;
    text-align: left;
    font-size: 14px;
    height: 36px;
    line-height: 20px;
    vertical-align: top;
  ]

  table.specification td, table.specification th [
    border: 1px solid gray;
    background-color: white;
  ]

  table.specification th [
    padding-right: 5px;
  ]

  </style>
</head>
<body>
  <h2>{item_name}</h2>
  <table class='information'>
    <tr> <td><b>Cena</b></td> <td>: <s>{old_price}</s> {new_price}</td> </tr>
    <tr> <td><b>Onionmeter</b></td> <td>: -{dif_price}zł </td> </tr>
  </table>
  <a href='{item_link}'>{item_image}</a>
  <h2>Specyfikacja:</h2>
  {item_specification}
</body>
</html>
"""

def format(*, item_name, old_price, new_price, dif_price, item_link, item_image, item_specification):
  mail_content.write( 
    mail.format(
      item_name = item_name,
      old_price = old_price,
      new_price = new_price,
      dif_price = dif_price,
      item_link = item_link,
      item_image = item_image, 
      item_specification = item_specification,
    ).replace('[','{').replace(']','}')
  )
  mail_content.seek(0)
  return mail_content.name
