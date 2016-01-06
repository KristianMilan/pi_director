<%inherit file="pi_director:templates/base.mak"/>
<%block name="BlockContent">

%if pis != None:
	<div class="container">
		<div class="row">
			<div class="col-lg-12">
				<h1>Current Fleet </h1>
			</div>
		%for pi in pis:
			<div class="col-lg-3 col-md-4 col-xs-6 thumb">
				<a class="thumbnail" href="#">
					<img class="img-responsive" src="${request.resource_url(request.context,'api/v1/screen/'+pi.uuid)}" alt="${pi.uuid}">
				</a>
			</div>	
		%endfor
		</div>
	</div>
%endif	

</%block>
