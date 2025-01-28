---
title: 
layout: withtable
---

This list ....

> Search the database for any keyword in any field.


<table class="display">
  <!-- Proj ID,Status,Title,RDC,Start Year,End Year,PI,Researcher -->
  {% for row in site.data.Researchers %}
    {% if forloop.first %}
    <thead>
    <tr>
      {% for cell in row %}
        {% if forloop.last %}
        <th>{{ cell[0] }}</th>
          {% continue %}
        {% else %}
        <th>{{ cell[0] }}</th>
        {% endif %}
      {% endfor %}
    </tr>
    </thead>
    {% endif %}

  <!-- manually constructing table -->
  <!-- Proj ID,Status,Title,RDC,Start Year,End Year,PI,Researcher -->
  <tr>
    <td> {{ row["Proj ID"] }} </td>
    <td> {{ row["PI"] }} </td>
    <td> {{ row["Researcher"] }} </td>
  </tr>
  {% endfor %}
</table>



To download the entire database, [click here].