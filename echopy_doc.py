import smartthings_settings as settings




navbar_titles=['Home','SmartThings','Nest']
navbar_links=[settings.full_root_url, settings.full_root_url,settings.full_root_url + '/nest']


###############################################################################
# NAVBAR 
###############################################################################

def navbar_generator(pageName):
	navbar_generated_links = ''
	for i,page in enumerate(navbar_titles):
		if pageName == page:
			navbar_generated_links += '\t\t\t\t<li class="active"><a href="' + navbar_links[i] +'">' + page + '''<span class="sr-only">(current)</span></a></li>''' + '\n'
		else:
			navbar_generated_links += '\t\t\t\t<li><a href="' + navbar_links[i] + '">' + page + '''</a></li>''' + '\n'
	return '''<title> ZP Alexa Projects - ''' + pageName + '''</title>''' + '\n' + html_navbar.replace('ZP_NAVBAR_GENERATED_LINKS',navbar_generated_links)


html_navbar='''
<nav class="navbar navbar-inverse">
	<div class="container-fluid">
		<!-- Brand and toggle get grouped for better mobile display -->
		<div class="navbar-header">
			<button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
				<span class="sr-only">Toggle navigation</span>
				<span class="icon-bar"></span>
				<span class="icon-bar"></span>
				<span class="icon-bar"></span>
			</button>
			<a class="navbar-brand" href="https://alexa.zpriddy.com">ZP Alexa Projects</a>
		</div>

		<!-- Collect the nav links, forms, and other content for toggling -->
		<div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
			<ul class="nav navbar-nav">
ZP_NAVBAR_GENERATED_LINKS
			</ul>
			<ul class="nav navbar-nav navbar-right">
				<li><a href="https://zpriddy.com">zpriddy.com</a></li>
			</ul>
		</div><!-- /.navbar-collapse -->
	</div><!-- /.container-fluid -->
</nav>
'''

###############################################################################
# Footer
###############################################################################


html_footer='''
<br><br><br>
<div class="navbar navbar-inverse navbar-fixed-bottom">
  <div class="container">
    <span class="navbar-text">
      <a href="''' + settings.full_root_url + '/privacy' + '''">Privacy Policy</a>
    </span>
  </div>
</div>
</html>
'''


###############################################################################
# Header
###############################################################################

html_header='''
<!DOCTYPE html>
<html lang="en">
<head>

  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>

  <script>
  (function(i,s,o,g,r,a,m){{i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){{
  (i[r].q=i[r].q||[]).push(arguments)}},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  }})(window,document,'script','//www.google-analytics.com/analytics.js','ga');

  ga('create', 'UA-65257509-1', 'auto');
  ga('send', 'pageview');

</script>

</head>

'''

###############################################################################
# PAGE GENERATOR 
###############################################################################
def page_generator(pageName,pageBody):
	generated_page= html_header + navbar_generator(pageName) + pageBody + html_footer

	return generated_page



###############################################################################
# Page Bodies  
###############################################################################

main_page_body='''
<div class="container">
	<div class="alert alert-info" role="alert">
		We currently have STCOUNT SmartThings users.
	</div>
	<div class="row">
		<div class="col-md-2"></div>
		<div class="col-md-8">
			<div class="jumbotron">
		    	<h2> Help Me Out!</h2>
		  	</div>
		  	<p>
		  	<p>Please consider helping me out so that I can keep supporting this and other Open Source projects! I run all of this out of my pocket and it doesnt all come free.. Please consider helping me out so that I can keep everything running!
		  	</p>
	    	<table>
			<td>
				<a class="btn btn-success" href="https://cash.me/$ZPriddy" >Support this project on Square Cash</a>
			</td>
			<td>
				&nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp;
			</td>
			<td>
				<p>
					<form action="https://www.paypal.com/cgi-bin/webscr" method="post" target="_top">
					<input type="hidden" name="cmd" value="_donations">
					<input type="hidden" name="business" value="paypal@zpriddy.com">
					<input type="hidden" name="lc" value="US">
					<input type="hidden" name="item_name" value="ZPriddy Alexa Projects">
					<input type="hidden" name="no_note" value="0">
					<input type="hidden" name="currency_code" value="USD">
					<input type="hidden" name="bn" value="PP-DonationsBF:btn_donate_LG.gif:NonHostedGuest">
					<input type="submit" name="submit"  class="btn btn-success" value="Support this project on PayPal">
					<img alt="" border="0" src="https://www.paypalobjects.com/en_US/i/scr/pixel.gif" width="1" height="1">
					</form>
				</p>
			</td>
		</table>

		</div>
	<div class="col-md-2"></div>
</div>

<div class="container">
<div class="panel panel-default">
		<div class="panel-heading">
			<h3 class="panel-title">Setting up Alexa with your SmartThings</h3>
		</div>
		<div class="panel-body">
	    	<p>To setup Alexa to talk to your SmartThings, Please follow the instructions: <a class="btn btn-warning" href="{0}/smartthings/setup" role="button">SmartThings Setup Instructions</a></p>
	    	<p>
			Supported Functions:
			<ul>
			<li> HelloHome - Executes HelloHome Action. 'Alexa, tell Smart Things to say I'm Home'</li>
			<li> Switches - 'Alexa, tell Smart Things to tuen off kitchen lights' </li>
			<li> Set Mode - 'Alexa, tell Smart Things to chnage Mode to movie' </li>
			</ul>
	    </p>
	    <p>
	    	The code that is running on this site is avilable here on <a href="https://github.com/zpriddy/ZP_EchoSmartThingsPy"> GitHub </a> I am always working on adding more features and will make announcements of new featuers that are added! 
	    </p>
		</div>
	</div>
	<div class="panel panel-default">
		<div class="panel-heading">
			<h3 class="panel-title">Quick Links</h3>
		</div>
		<div class="panel-body">

			<a class="btn btn-success" href="{0}/auth" role="button">SmartThings Alexa Auth</a>
			<a class="btn btn-info" href="{0}/samples" role="button">SmartThings Alexa Smaples</a>
		</div>
	</div>
</div>
'''

st_setup_page_body='''
<div class="container">
	<div class="alert alert-danger alert-dismissible" role="alert">
		<button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button>
		<p><strong>Please consider supporting this project!</strong> Donations can be made in any amount via Square Cash with no fees or on PayPal</p> 
		<table>
			<td>
				<a class="btn btn-success" href="https://cash.me/$ZPriddy" >Support this project on Square Cash</a>
			</td>
			<td>
				&nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp;
			</td>
			<td>
				<p>
					<form action="https://www.paypal.com/cgi-bin/webscr" method="post" target="_top">
					<input type="hidden" name="cmd" value="_donations">
					<input type="hidden" name="business" value="paypal@zpriddy.com">
					<input type="hidden" name="lc" value="US">
					<input type="hidden" name="item_name" value="ZPriddy Alexa Projects">
					<input type="hidden" name="no_note" value="0">
					<input type="hidden" name="currency_code" value="USD">
					<input type="hidden" name="bn" value="PP-DonationsBF:btn_donate_LG.gif:NonHostedGuest">
					<input type="submit" name="submit"  class="btn btn-success" value="Support this project on PayPal">
					<img alt="" border="0" src="https://www.paypalobjects.com/en_US/i/scr/pixel.gif" width="1" height="1">
					</form>
				</p>
			</td>
		</table>
	</div>

	<div class="panel panel-default">
		<!-- Default panel contents -->
		<div class="panel-heading">Step 1: Amazon Echo Setup</div>
		<div class="panel-body">
	    <p>At this point in time you will need to create an Amazon developer account with the same Amazon account that is used for your Amazon Echo. Follow the steps below to do so.</p>
		</div>

		<!-- List group -->
		<ul class="list-group">
			<li class="list-group-item">Go to the Amazon developer portal: <a href="https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit"> Amazon Alexa Portal</a></li>
			<li class="list-group-item">At the top of the page click on 'SIGN IN or CREATE FREE ACCOUNT'</li>
			<li class="list-group-item">Login with youe Amazon ID</li>
			<li class="list-group-item">Go to Apps & Services at the top of the page</li>
			<li class="list-group-item">Click on Alexa</li>
			<li class="list-group-item">Click on Alexa Skills Kit</li>
			<li class="list-group-item">Click Add New Skill</li>
			<li class="list-group-item">Fill out the first form:<br>-Name: Anything you want it to be - I use Smart Things Control<br>-Invocation Name: The hotword to call the app - I have gotten it working with Smart Things<br>-Version: 1.0 <- This is hard-coded for now<br>-Endpoint: https://alexa.zpriddy.com/alexa/EchoPyAPI</li>
			<li class="list-group-item">Click on Next</li>
			<li class="list-group-item">Copy the content of <a href="{0}/smartthings/static/intentSchema.json">this page</a> into the Intent Schema</li>
			<li class="list-group-item">Copy the content of <a href="{0}/smartthings/static/sampleUtterances.txt">this page</a> into the Sample Utterances</li>
			<li class="list-group-item">Click on Next</li>
			<li class="list-group-item">Click on 'My development endpoint has a certificate from a trusted certificate authority (required for certification)'</li>
			<li class="list-group-item">Click on Next</li>
			<li class="list-group-item">Make sure that the skill is enabled</li>
			<li class="list-group-item">Click on Next</li>
			<li class="list-group-item">DO NOT Submit for Certification. Don't close this windo, you will need it again at the end.</li>
		</ul>
	</div>


	<div class="panel panel-default">
		<!-- Default panel contents -->
		<div class="panel-heading">Step 2: SmartThings Setup</div>
		<div class="panel-body">
	    <p>To get PyDash to talk to your SmartThings devices, you need to create a SmartApp that will serve as an API. </p>
		</div>

		<!-- List group -->
		<ul class="list-group">
			<li class="list-group-item">Go to <a href="https://graph.api.smartthings.com"> SmartThings IDE </a> and log in to your SmartThings IDE account.</li>
			<li class="list-group-item">Click on 'MySmartApps' tab</li>
			<li class="list-group-item">Click on '+NewSmartApp' button</li>
			<li class="list-group-item">Fill in the required information. The 'Name'and 'Description' are both required fields, but their values are not important.</li>
			<li class="list-group-item">Click the 'Enable OAuth in Smart App' button to grant REST API access to the new SmartApp. Note the 'OAuth Client ID' and 'OAuth Client Secret'. Both will later be required by the Alexa backend to authenticate with the new SmartApp and talk to SmartThings.</li>
			<li class="list-group-item">Click the 'Create' button to get to the code editor. </li>
			<li class="list-group-item">Copy the content of <a href="{0}/smartthings/static/alexaAccess.txt">this page</a> into the SmartApp</li>
			<li class="list-group-item">Click the 'Save' button and then 'Publish -> For Me'.</li>
		</ul>
	</div>

	<div class="panel panel-default">
		<!-- Default panel contents -->
		<div class="panel-heading">Step 3: Link your SmartThings to Alexa</div>
		<div class="panel-body">
	    <p>Follow the steps below to connect your Smart Things accoutn to your Amazon Echo</p>
		</div>

		<!-- List group -->
		<ul class="list-group">
			<li class="list-group-item">Ask your Alexa to talk to SmartThings by saying: 'Alexa, Talk to Smart Things' (If you didnt use Smart Things as your invocation name, you will have to replace Smart Things with the invocation name you used)</li>
			<li class="list-group-item">Open the Echo app in your phone, You should see a 10 digit Alexa ID. This ID is One Time Use Only.</li>
			<li class="list-group-item">Go to the <a href="{0}/auth">SmartThings Auth Page</a></li>
			<li class="list-group-item">Enter your Alexa ID, OAuth Client ID, OAuth Client Secret (From previous step in the SmartThings IDE) and your Email Address</li>
			<li class="list-group-item">Click on Authorize</li>
			<li class="list-group-item">You will be asked to log in to your SmartThings account. Select the devices that you would like Alexa to be able to control.</li>
			
		</ul>
	</div>

	<div class="panel panel-default">
		<!-- Default panel contents -->
		<div class="panel-heading">Step 4: Customized Sample Utterances</div>
		<div class="panel-body">
	    <p>Follow the steps below to get your customized sample utterances</p>
		</div>

		<!-- List group -->
		<ul class="list-group">
			<li class="list-group-item">Ask your Alexa for a new AlexaID by saying: 'Alexa, Tell Smart Things to give me a new alexa ID' (If you didnt use Smart Things as your invocation name, you will have to replace Smart Things with the invocation name you used)</li>
			<li class="list-group-item">Open the Echo app in your phone, You should see a 10 digit Alexa ID. This ID is One Time Use Only. This will be different than the last one you used.</li>
			<li class="list-group-item">Go to the <a href="{0}/samples">SmartThings Samples Page</a></li>
			<li class="list-group-item">Enter your Alexa ID</li>
			<li class="list-group-item">Click on Get Samples</li>
			<li class="list-group-item">Highlight and copy the text that is displayed in the blue box.</li>
			<li class="list-group-item">Go to the Amazon developer portal If you still have this open you can skip the next 6 steps. <a href="https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit"> Amazon Alexa Portal</a></li>
			<li class="list-group-item">At the top of the page click on 'SIGN IN or CREATE FREE ACCOUNT'</li>
			<li class="list-group-item">Login with youe Amazon ID</li>
			<li class="list-group-item">Go to Apps & Services at the top of the page</li>
			<li class="list-group-item">Click on Alexa</li>
			<li class="list-group-item">Click on Alexa Skills Kit</li>
			<li class="list-group-item">Click edit on the skill that you already created</li>
			<li class="list-group-item">Click on Interaction Modle on the left</li>
			<li class="list-group-item">Paste the output of the samples page into the Sample Utterances</li>
			<li class="list-group-item">Done</li>

		</ul>
	</div>




</div>
'''

auth_page_body='''
<div class="container">
	<div class="alert alert-danger alert-dismissible" role="alert">
		<button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button>
		<p><strong>Please consider supporting this project!</strong> Donations can be made in any amount via Square Cash with no fees or on PayPal</p> 
		<table>
			<td>
				<a class="btn btn-success" href="https://cash.me/$ZPriddy" >Support this project on Square Cash</a>
			</td>
			<td>
				&nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp;
			</td>
			<td>
				<p>
					<form action="https://www.paypal.com/cgi-bin/webscr" method="post" target="_top">
					<input type="hidden" name="cmd" value="_donations">
					<input type="hidden" name="business" value="paypal@zpriddy.com">
					<input type="hidden" name="lc" value="US">
					<input type="hidden" name="item_name" value="ZPriddy Alexa Projects">
					<input type="hidden" name="no_note" value="0">
					<input type="hidden" name="currency_code" value="USD">
					<input type="hidden" name="bn" value="PP-DonationsBF:btn_donate_LG.gif:NonHostedGuest">
					<input type="submit" name="submit"  class="btn btn-success" value="Support this project on PayPal">
					<img alt="" border="0" src="https://www.paypalobjects.com/en_US/i/scr/pixel.gif" width="1" height="1">
					</form>
				</p>
			</td>
		</table>
	</div>
	<form action="auth" method="post">
		<div class="form-group required">
			<label for="AlexaID">Alexa ID</label>
			<input id="AlexaID" name="AlexaID" type="text" class="form-control" title="Alexa ID. This is a required field" required="required">
		</div>
		<div class="form-group required">
			<label for="SmartThingsClientID">SmartThings Client ID</label>
			<input id="SmartThingsClientID" name="SmartThingsClientID" type="text" class="form-control" title="SmartThings Client ID. This is a required field" required="required">
		</div>
		<div class="form-group required">
			<label for="SmartThingsClientSecret">SmartThings Client Secret </label>
			<input id="SmartThingsClientSecret" name="SmartThingsClientSecret" type="text" class="form-control" title="SmartThings Client Secret . This is a required field" required="required">
		</div>
		<div class="form-group required">
		  <label for="SmartThingsClientSecret">Email Address - This is used for notication and support only! </label>
		  <input id="Email" name="Email" type="email" class="form-control" title="Email Address - This is used for notication and support only! . This is a required field" required="required">
		</div>
		<input type="submit" value="Authorize" class="btn btn-default">
	</form>
</div>
'''

nest_auth_page_body='''
<div class="container">
	<div class="alert alert-info" role="alert">
		Currently we can only support 1000 Nest users. We currently have NESTCOUNT users.
	</div>
	<div class="alert alert-danger alert-dismissible" role="alert">
		<button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button>
		<p><strong>Please consider supporting this project!</strong> Donations can be made in any amount via Square Cash with no fees or on PayPal</p> 
		<table>
			<td>
				<a class="btn btn-success" href="https://cash.me/$ZPriddy" >Support this project on Square Cash</a>
			</td>
			<td>
				&nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp;
			</td>
			<td>
				<p>
					<form action="https://www.paypal.com/cgi-bin/webscr" method="post" target="_top">
					<input type="hidden" name="cmd" value="_donations">
					<input type="hidden" name="business" value="paypal@zpriddy.com">
					<input type="hidden" name="lc" value="US">
					<input type="hidden" name="item_name" value="ZPriddy Alexa Projects">
					<input type="hidden" name="no_note" value="0">
					<input type="hidden" name="currency_code" value="USD">
					<input type="hidden" name="bn" value="PP-DonationsBF:btn_donate_LG.gif:NonHostedGuest">
					<input type="submit" name="submit"  class="btn btn-success" value="Support this project on PayPal">
					<img alt="" border="0" src="https://www.paypalobjects.com/en_US/i/scr/pixel.gif" width="1" height="1">
					</form>
				</p>
			</td>
		</table>
	</div>
	<form action="auth" method="post">
		<div class="form-group required">
			<label for="AlexaID">Alexa ID</label>
			<input id="AlexaID" name="AlexaID" type="text" class="form-control" title="Alexa ID. This is a required field" required="required">
		</div>
		<div class="form-group required">
		  <label for="SmartThingsClientSecret">Email Address - This is used for notication and support only! </label>
		  <input id="Email" name="Email" type="email" class="form-control" title="Email Address - This is used for notication and support only! . This is a required field" required="required">
		</div>
		<input type="submit" value="Authorize" class="btn btn-default">
	</form>
</div>
'''


nest_setup_page_body='''
<div class="container">
	<div class="alert alert-info" role="alert">
		Currently we can only support 1000 Nest users. We currently have NESTCOUNT users.
	</div>
	<div class="alert alert-danger alert-dismissible" role="alert">
		<button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button>
		<p><strong>Please consider supporting this project!</strong> Donations can be made in any amount via Square Cash with no fees or on PayPal</p> 
		<table>
			<td>
				<a class="btn btn-success" href="https://cash.me/$ZPriddy" >Support this project on Square Cash</a>
			</td>
			<td>
				&nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp;
			</td>
			<td>
				<p>
					<form action="https://www.paypal.com/cgi-bin/webscr" method="post" target="_top">
					<input type="hidden" name="cmd" value="_donations">
					<input type="hidden" name="business" value="paypal@zpriddy.com">
					<input type="hidden" name="lc" value="US">
					<input type="hidden" name="item_name" value="ZPriddy Alexa Projects">
					<input type="hidden" name="no_note" value="0">
					<input type="hidden" name="currency_code" value="USD">
					<input type="hidden" name="bn" value="PP-DonationsBF:btn_donate_LG.gif:NonHostedGuest">
					<input type="submit" name="submit"  class="btn btn-success" value="Support this project on PayPal">
					<img alt="" border="0" src="https://www.paypalobjects.com/en_US/i/scr/pixel.gif" width="1" height="1">
					</form>
				</p>
			</td>
		</table>
	</div>

	<div class="panel panel-default">
		<!-- Default panel contents -->
		<div class="panel-heading">Step 1: Amazon Echo Setup</div>
		<div class="panel-body">
	    <p>At this point in time you will need to create an Amazon developer account with the same Amazon account that is used for your Amazon Echo. Follow the steps below to do so.</p>
		</div>

		<!-- List group -->
		<ul class="list-group">
			<li class="list-group-item">Go to the Amazon developer portal: <a href="https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit"> Amazon Alexa Portal</a></li>
			<li class="list-group-item">At the top of the page click on 'SIGN IN or CREATE FREE ACCOUNT'</li>
			<li class="list-group-item">Login with youe Amazon ID</li>
			<li class="list-group-item">Go to Apps & Services at the top of the page</li>
			<li class="list-group-item">Click on Alexa</li>
			<li class="list-group-item">Click on Alexa Skills Kit</li>
			<li class="list-group-item">Click Add New Skill</li>
			<li class="list-group-item">Fill out the first form:<br>-Name: Anything you want it to be - I use Nest Control<br>-Invocation Name: The hotword to call the app - I have gotten it working with Nest<br>-Version: 1.0 <- This is hard-coded for now<br>-Endpoint: https://alexa.zpriddy.com/alexa/nest/EchoPyAPI</li>
			<li class="list-group-item">Click on Next</li>
			<li class="list-group-item">Copy the content of <a href="{0}/nest/static/intentSchema.json">this page</a> into the Intent Schema</li>
			<li class="list-group-item">Copy the content of <a href="{0}/nest/static/sampleUtterances.txt">this page</a> into the Sample Utterances</li>
			<li class="list-group-item">Click on Next</li>
			<li class="list-group-item">Click on 'My development endpoint has a certificate from a trusted certificate authority (required for certification)'</li>
			<li class="list-group-item">Click on Next</li>
			<li class="list-group-item">Make sure that the skill is enabled</li>
			<li class="list-group-item">Click on Next</li>
			<li class="list-group-item">At this point you can close the amazon developer portal. DO NOT Submit for Certification</li>
		</ul>
	</div>

	<div class="panel panel-default">
		<!-- Default panel contents -->
		<div class="panel-heading">Step 2: Link your Nest to Alexa</div>
		<div class="panel-body">
	    <p>Follow the steps below to connect your nest thermostat to your Amazon Echo</p>
		</div>

		<!-- List group -->
		<ul class="list-group">
			<li class="list-group-item">Ask your Alexa to talk to Nest by saying: 'Alexa, Talk to Nest' (If you didnt use Nest as your invocation name, you will have to replace Nest with the invocation name you used)</li>
			<li class="list-group-item">Open the Echo app in your phone, You should see a 10 digit Alexa ID. This ID is One Time Use Only.</li>
			<li class="list-group-item">Go to the <a href="{0}/nest/auth">Nest Auth Page</a></li>
			<li class="list-group-item">Enter your Alexa ID and your Email address</li>
			<li class="list-group-item">Click on Authorize</li>
			<li class="list-group-item">You will be asked to log in to your Nest account. Confirm that you are wanting to link the app to your Nest</li>
			<li class="list-group-item">Done!</li>
		</ul>
	</div>


</div>
'''

nest_page_body='''
<div class="container">
	<div class="alert alert-info" role="alert">
			We currently have NESTCOUNT Nest users.
	</div>
	<div class="row">
		<div class="col-md-2"></div>
		<div class="col-md-8">
			<div class="jumbotron">
		    	<h2> Help Me Out!</h2>
		  	</div>
		  	<p>
		  	<p>Please consider helping me out so that I can keep supporting this and other Open Source projects! I run all of this out of my pocket and it doesnt all come free.. Please consider helping me out so that I can keep everything running!
		  	</p>
	    	<table>
			<td>
				<a class="btn btn-success" href="https://cash.me/$ZPriddy" >Support this project on Square Cash</a>
			</td>
			<td>
				&nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp;
			</td>
			<td>
				<p>
					<form action="https://www.paypal.com/cgi-bin/webscr" method="post" target="_top">
					<input type="hidden" name="cmd" value="_donations">
					<input type="hidden" name="business" value="paypal@zpriddy.com">
					<input type="hidden" name="lc" value="US">
					<input type="hidden" name="item_name" value="ZPriddy Alexa Projects">
					<input type="hidden" name="no_note" value="0">
					<input type="hidden" name="currency_code" value="USD">
					<input type="hidden" name="bn" value="PP-DonationsBF:btn_donate_LG.gif:NonHostedGuest">
					<input type="submit" name="submit"  class="btn btn-success" value="Support this project on PayPal">
					<img alt="" border="0" src="https://www.paypalobjects.com/en_US/i/scr/pixel.gif" width="1" height="1">
					</form>
				</p>
			</td>
		</table>

		</div>
	<div class="col-md-2"></div>
</div>

<div class="container">
	<div class="panel panel-default">
		<div class="panel-heading">
			<h3 class="panel-title">Setting up Alexa with your Nest</h3>
		</div>
    <div class="panel-body">
    <p>To setup Alexa to talk to your Nest, Please follow the instructions: <a class="btn btn-warning" href="{0}/nest/setup" role="button">Nest Setup Instructions</a></p>
    <p>
    Supported Functions:
    <ul>
    	<li> Set Temperature - Sets all Nests to the given temperature in F. 'Alexa, tell Nest to set temperature to 74'</li>
    	<li> Chnage Temperature by 2 degrees - 'Alexa, tell Nest that I'm a little warm' </li>
    	<li> Set Mode - Sets all structurs to selected mode. 'Alexa, tell Nest goodbye', 'Alexa, tell Nest to set mode to Home' </li>
    </ul>

    </p>

    
	</div>
</div>
	<div class="panel panel-default">
		<div class="panel-heading">
			<h3 class="panel-title">Quick Links</h3>
		</div>
	<div class="panel-body">

		<a class="btn btn-success" href="{0}/nest/auth" role="button">Nest Alexa Auth</a>
	</div>
</div>



'''


samples_page_body='''
<div class="container">
	<div class="alert alert-danger alert-dismissible" role="alert">
		<button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button>
		<p><strong>Please consider supporting this project!</strong> Donations can be made in any amount via Square Cash with no fees! </p> 
		<a class="btn btn-success" href="https://cash.me/$ZPriddy" >Support this project on Square Cash</a>
	</div>
	<form action="samples" method="post">
		<div class="form-group">
			<label for="AlexaID">Alexa ID</label>
			<input id="AlexaID" name="AlexaID" type="text" class="form-control" title="Alexa ID. This is a required field">
		</div>
	<input type="submit" value="Get Samples" class="btn btn-default">
	</form>
</div>
'''

samples_results_body='''
<div class="container">
	<h1>Sample Resultss</h1>
	<p> Please copy and paste the results below into your Alexa SampleUtterances in the ASK portal. </p>
	<div class="panel panel-primary">
		<div class="panel-heading">Sample</div>
		<div class="panel-body" style="max-height: 500px;overflow-y: scroll;">RESULTS</div>
	</div>
</div>
'''


html_privacy_policy_body='''
<div class="container">
<h1><strong>alexa.zpriddy.com Privacy Policy</strong></h1><p>
This privacy policy has been compiled to better serve those who are concerned with how their &#8216;Personally identifiable information&#8217; (PII) is being used online. PII, as used in US privacy law and information security, is information that can be used on its own or with other information to identify, contact, or locate a single person, or to identify an individual in context. Please read our privacy policy carefully to get a clear understanding of how we collect, use, protect or otherwise handle your Personally Identifiable Information in accordance with our website.</p>

<p><strong><em>What personal information do we collect from the people that visit our blog, website or app?</em></strong></p>

<p>When registering on our site, as appropriate, you may be asked to enter your email address or other details to help you with your experience.</p>

<p><strong><em>When do we collect information?</em></strong></p>

<p>We collect information from you when you register on our site or enter information on our site.</p>

<p><strong><em>How do we use your information?</em></strong></p>

<p>We may use the information we collect from you when you register, sign up for our newsletter, surf the website, or use certain other site features in the following ways:</p>

<p>
&bull; To improve our website in order to better serve you.<br>
&bull; To allow us to better service you in responding to your customer service requests.<br>
</p>

<p><strong><em>How do we protect visitor information?</em></strong></p>

<p>Our website is scanned on a regular basis for security holes and known vulnerabilities in order to make your visit to our site as safe as possible.</p>

<p>We use regular Malware Scanning.</p>

<p>Your personal information is contained behind secured networks and is only accessible by a limited number of persons who have special access rights to such systems, and are required to keep the information confidential. In addition, all sensitive/credit information you supply is encrypted via Secure Socket Layer (SSL) technology.</p>

<p>We implement a variety of security measures when a user enters, submits, or accesses their information to maintain the safety of your personal information.</p>

<p>All transactions are processed through a gateway provider and are not stored or processed on our servers.</p>

<p><strong><em>Do we use &#8216;cookies&#8217;?</em></strong></p>

<p>We do use cookies for tracking purposes</p>

<p>You can choose to have your computer warn you each time a cookie is being sent, or you can choose to turn off all cookies. You do this through your browser (like Internet Explorer) settings. Each browser is a little different, so look at your browser&#8217;s Help menu to learn the correct way to modify your cookies.</p>

<p>If you disable cookies off, some features will be disabled that make your site experience more efficient and some of our services will not function properly.</p>

<p><strong><em>Third Party Disclosure</em></strong></p>

<p>We do not sell, trade, or otherwise transfer to outside parties your personally identifiable information unless we provide you with advance notice. This does not include website hosting partners and other parties who assist us in operating our website, conducting our business, or servicing you, so long as those parties agree to keep this information confidential. We may also release your information when we believe release is appropriate to comply with the law, enforce our site policies, or protect ours or others&#8217; rights, property, or safety. </p>

<p><strong><em>Third party links</em></strong></p>

<p>Occasionally, at our discretion, we may include or offer third party products or services on our website. These third party sites have separate and independent privacy policies. We therefore have no responsibility or liability for the content and activities of these linked sites. Nonetheless, we seek to protect the integrity of our site and welcome any feedback about these sites.</p>

<p><strong><em>Google</em></strong></p>

<p>Google&#8217;s advertising requirements can be summed up by Google&#8217;s Advertising Principles. They are put in place to provide a positive experience for users. https://support.google.com/adwordspolicy/answer/1316548?hl=en </p>

<p>We use Google Analytics on our website.</p>

<p>Google, as a third party vendor, uses cookies to serve ads on our site. Google&#8217;s use of the DART cookie enables it to serve ads to our users based on their visit to our site and other sites on the Internet. Users may opt out of the use of the DART cookie by visiting the Google ad and content network privacy policy.</p>

<p>We have implemented the following:<br>
 &bull; Demographics and Interests Reporting</p>

<p>We along with third-party vendors, such as Google use first-party cookies (such as the Google Analytics cookies) and third-party cookies (such as the DoubleClick cookie) or other third-party identifiers together to compile data regarding user interactions with ad impressions, and other ad service functions as they relate to our website.</p>

<p>Opting out:<br>
Users can set preferences for how Google advertises to you using the Google Ad Settings page. Alternatively, you can opt out by visiting the Network Advertising initiative opt out page or permanently using the Google Analytics Opt Out Browser add on.</p>

<p>California Online Privacy Protection Act</p>

<p>CalOPPA is the first state law in the nation to require commercial websites and online services to post a privacy policy. The law&#8217;s reach stretches well beyond California to require a person or company in the United States (and conceivably the world) that operates websites collecting personally identifiable information from California consumers to post a conspicuous privacy policy on its website stating exactly the information being collected and those individuals with whom it is being shared, and to comply with this policy. - See more at: http://consumercal.org/california-online-privacy-protection-act-caloppa/#sthash.0FdRbT51.dpuf</p>

<p>According to CalOPPA we agree to the following:
Users can visit our site anonymously<br>
Once this privacy policy is created, we will add a link to it on our home page, or as a minimum on the first significant page after entering our website.<br>
Our Privacy Policy link includes the word &#8216;Privacy&#8217;, and can be easily be found on the page specified above.<br></p>

<p>Users will be notified of any privacy policy changes:<br>
 &bull; Via Email<br>
Users are able to change their personal information:<br>
 &bull; By emailing us<br>
 &bull; By chatting with us or sending us a ticket<br></p>

<p>How does our site handle do not track signals?
We honor do not track signals and do not track, plant cookies, or use advertising when a Do Not Track (DNT) browser mechanism is in place.</p>

<p>Does our site allow third party behavioral tracking?
It&#8217;s also important to note that we allow third party behavioral tracking</p>

<p><strong><em>COPPA (Children Online Privacy Protection Act)</em></strong></p>

<p>When it comes to the collection of personal information from children under 13, the Children&#8217;s Online Privacy Protection Act (COPPA) puts parents in control. The Federal Trade Commission, the nation&#8217;s consumer protection agency, enforces the COPPA Rule, which spells out what operators of websites and online services must do to protect children&#8217;s privacy and safety online.</p>

<p>We do not specifically market to children under 13.</p>

<p><strong><em>Fair Information Practices</em></strong></p>

<p>The Fair Information Practices Principles form the backbone of privacy law in the United States and the concepts they include have played a significant role in the development of data protection laws around the globe. Understanding the Fair Information Practice Principles and how they should be implemented is critical to comply with the various privacy laws that protect personal information.</p>

<p>In order to be in line with Fair Information Practices we will take the following responsive action, should a data breach occur:
We will notify the users via email<br>
 &bull; Within 1 business day<br>
We will notify the users via in site notification<br>
 &bull; Within 1 business day<br></p>

<p>We also agree to the individual redress principle, which requires that individuals have a right to pursue legally enforceable rights against data collectors and processors who fail to adhere to the law. This principle requires not only that individuals have enforceable rights against data users, but also that individuals have recourse to courts or a government agency to investigate and/or prosecute non-compliance by data processors.</p>

<p><strong><em>CAN SPAM Act</em></strong></p>

<p>The CAN-SPAM Act is a law that sets the rules for commercial email, establishes requirements for commercial messages, gives recipients the right to have emails stopped from being sent to them, and spells out tough penalties for violations.</p>

<p>We collect your email address in order to:
 & bull; Send information, respond to inquiries, and/or other requests or questions.</p>

<p>To be in accordance with CANSPAM we agree to the following:<br>

 &bull; NOT use false, or misleading subjects or email addresses<br>
 &bull; Identify the message as an advertisement in some reasonable way<br>
 &bull; Include the physical address of our business or site headquarters<br>
 &bull; Monitor third party email marketing services for compliance, if one is used.<br>
 &bull; Honor opt-out/unsubscribe requests quickly<br>
 &bull; Allow users to unsubscribe by using the link at the bottom of each email<br></p>

<p>If at any time you would like to unsubscribe from receiving future emails, you can email us at <br>
 &bull; Follow the instructions at the bottom of each email.<br>
and we will promptly remove you from ALL correspondence.</p>

<p><strong><em>Contacting Us</em></strong></p>

<p>If there are any questions regarding this privacy policy you may contact us using the information below.</p>

<p>Zachary Priddy
alexa@zpriddy.com</p>

<p>Last Edited on 2015&#8211;08&#8211;11</p>
</div>
'''



###############################################################################
# PAGES 
###############################################################################

#main_page = page_generator('Home',main_page_body)
auth_page = page_generator('Auth',auth_page_body)
samples_page = page_generator('Request Samples',samples_page_body)
samples_results = page_generator('Sample Results',samples_results_body)
privacy_policy = page_generator('Privacy Policy',html_privacy_policy_body)
st_setup_page = page_generator('SmartThings Setup',st_setup_page_body)

def nest_setup_page(count):
	return page_generator('Nest Setup',nest_setup_page_body).replace('NESTCOUNT',str(count))

def nest_page(count):
	return page_generator('Nest',nest_page_body).replace('NESTCOUNT',str(count))

def main_page(count):
	return page_generator('Home',main_page_body).replace('STCOUNT', str(count))

def st_main_page(count):
	return page_generator('SmartThings',main_page_body).replace('STCOUNT', str(count))

def nest_auth_page(count):
	return page_generator('Auth',nest_auth_page_body).replace('NESTCOUNT',str(count))

NotNestUser = {"outputSpeech": {"type":"PlainText","text":"Current user is not a valid nest user. Please look for help"},"card":{"type":"Simple","title":"Nest Control Error","content":"Current user is not a valid nest user. Please look for help"},'shouldEndSession':True}