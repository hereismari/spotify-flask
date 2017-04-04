{% extends "layout.html" %}

{% block content %}

{% if not user %}

  <div class="container">
    <div class="mt-1">
      <h1>Profile</h1>
    </div>
    <p class="lead">You need to log in to see this page</p>

    <a type="button" class="btn btn-default" href="/auth">Login</a>
  </div>

{% else %}

	<div class="container">


	  <h1> Hi {{ user.display_name }} :) </h1>

    <hr class="half-rule"/>

	  <div class="row">
      <div class="col-sm-4">

        <section class="sec">

          {% if user.images %}
            <img src="{{user.images[0].url}}" class="img-square">
          {% else %}
            <img src="http://bit.ly/2nXRRfX" class="img-square">
          {% endif %}

          <h3>You have {{ user.followers.total }} followers!</h3>
        </section>
      </div>

      <div class="col-sm-4">

        <h3> Your playlists: </h3>
        <hr class="half-rule"/>

        {% for play in playlists %}
          <div class='row'>
            <a href="{{ play.external_urls.spotify }}">

              <div class='col-sm-8'>
                <span>{{ play.name }} </span>
              </div>

            </a>
          </div>
        {% endfor %}
      </div>
<!--
      <div class="col-sm-4">

        <h3> Your top artist: </h3>
        <hr class="half-rule"/>

        {% for artist in top_artists %}
          <div class='row'>
            <a href="{{url_for('artist', id=artist.id) }}">

              <div class='col-sm-8'>
                <span>{{ artist.name }} </span>
              </div>

            </a>
          </div>
        {% endfor %}
      </div> -->

      <div class="col-sm-4">

        <h3> Recently played:</h3>
        <hr class="half-rule"/>

        {% for track in recently_played %}
          <div class='row'>
            <a href="{{track.track.external_urls.spotify}}">

              <div class='col-sm-8'>
                <span>{{track.track.name}}</span>
              </div>

            </a>
          </div>
        {% endfor %}
      </div>

    </div>
	</div>

{% endif %}

{% endblock %}
