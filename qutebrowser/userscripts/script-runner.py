<!DOCTYPE html>
<html lang="en-US" data-theme="codeberg-auto">
<head>
	<meta name="viewport" content="width=device-width, initial-scale=1">
	
	<title>qutebrowser-metascript/script-runner.py at master - mister_monster/qutebrowser-metascript - Codeberg.org</title>
	<link rel="manifest" href="data:application/json;base64,eyJuYW1lIjoiQ29kZWJlcmcub3JnIiwic2hvcnRfbmFtZSI6IkNvZGViZXJnLm9yZyIsInN0YXJ0X3VybCI6Imh0dHBzOi8vY29kZWJlcmcub3JnLyIsImljb25zIjpbeyJzcmMiOiJodHRwczovL2NvZGViZXJnLm9yZy9hc3NldHMvaW1nL2xvZ28ucG5nIiwidHlwZSI6ImltYWdlL3BuZyIsInNpemVzIjoiNTEyeDUxMiJ9LHsic3JjIjoiaHR0cHM6Ly9jb2RlYmVyZy5vcmcvYXNzZXRzL2ltZy9sb2dvLnN2ZyIsInR5cGUiOiJpbWFnZS9zdmcreG1sIiwic2l6ZXMiOiI1MTJ4NTEyIn1dfQ==">
	<meta name="author" content="mister_monster">
	<meta name="description" content="qutebrowser-metascript - A user configurable arbitrary sequential command running userscript for Qutebrowser, written in Python.">
	<meta name="keywords" content="git,non-profit,foss,oss,free,software,open,source,code,hosting">
	<meta name="referrer" content="no-referrer">


	<link rel="alternate" type="application/atom+xml" title="" href="/mister_monster/qutebrowser-metascript.atom">
	<link rel="alternate" type="application/rss+xml" title="" href="/mister_monster/qutebrowser-metascript.rss">

	<link rel="icon" href="/assets/img/favicon.svg" type="image/svg+xml">
	<link rel="alternate icon" href="/assets/img/favicon.png" type="image/png">
	
<script>
	
	window.addEventListener('error', function(e) {window._globalHandlerErrors=window._globalHandlerErrors||[]; window._globalHandlerErrors.push(e);});
	window.addEventListener('unhandledrejection', function(e) {window._globalHandlerErrors=window._globalHandlerErrors||[]; window._globalHandlerErrors.push(e);});
	window.config = {
		appUrl: 'https:\/\/codeberg.org\/',
		appSubUrl: '',
		assetVersionEncoded: encodeURIComponent('9.0.0-226-28dcc7f11a~gitea-1.22.0'), 
		assetUrlPrefix: '\/assets',
		runModeIsProd:  true ,
		customEmojis: {"codeberg":":codeberg:","forgejo":":forgejo:","git":":git:","gitea":":gitea:","github":":github:","gitlab":":gitlab:","gogs":":gogs:"},
		csrfToken: 'Whc5wbMhhn77X832VltZ_mzf0qA6MTczNTI0MDYzOTI4MjM1NjQxNQ',
		pageData: {},
		notificationSettings: {"EventSourceUpdateTime":10000,"MaxTimeout":60000,"MinTimeout":10000,"TimeoutStep":10000}, 
		enableTimeTracking:  true ,
		
		mermaidMaxSourceCharacters:  5000 ,
		
		i18n: {
			copy_success: "Copied!",
			copy_error: "Copy failed",
			error_occurred: "An error occurred",
			network_error: "Network error",
			remove_label_str: "Remove item \"%s\"",
			modal_confirm: "Confirm",
			modal_cancel: "Cancel",
			more_items: "More items",
		},
	};
	
	window.config.pageData = window.config.pageData || {};
</script>
<script src="/assets/js/webcomponents.js?v=9.0.0-226-28dcc7f11a~gitea-1.22.0"></script>

	<noscript>
		<style>
			.dropdown:hover > .menu { display: block; }
			.ui.secondary.menu .dropdown.item > .menu { margin-top: 0; }
		</style>
	</noscript>
	
	
		<meta property="og:title" content="qutebrowser-metascript/script-runner.py at master">
		<meta property="og:url" content="https://codeberg.org//mister_monster/qutebrowser-metascript/src/branch/master/script-runner.py">
		
	
	<meta property="og:type" content="object">
	
		<meta property="og:image" content="https://codeberg.org/avatars/22d4d12a0a0deaaeb4d611106ffdac8e">
	

<meta property="og:site_name" content="Codeberg.org">

	<link rel="stylesheet" href="/assets/css/index.css?v=9.0.0-226-28dcc7f11a~gitea-1.22.0">
<link rel="stylesheet" href="/assets/css/theme-codeberg-auto.css?v=9.0.0-226-28dcc7f11a~gitea-1.22.0">

	
</head>
<body hx-headers='{"x-csrf-token": "Whc5wbMhhn77X832VltZ_mzf0qA6MTczNTI0MDYzOTI4MjM1NjQxNQ"}' hx-swap="outerHTML" hx-ext="morph" hx-push-url="false">
	

	<div class="full height">
		<noscript>This website requires JavaScript.</noscript>

		

		
			


<nav id="navbar" aria-label="Navigation bar">
	<div class="navbar-left ui secondary menu">
		
		<a class="item" id="navbar-logo" href="/" aria-label="Home">
			<img width="30" height="30" src="https://design.codeberg.org/logo-kit/icon_inverted.svg" aria-hidden="true">
		</a>

		
		<div class="ui secondary menu item navbar-mobile-right only-mobile">
			
			<button class="item tw-w-auto ui icon mini button tw-p-2 tw-m-0" id="navbar-expand-toggle" aria-label="Toggle menu"><svg viewBox="0 0 16 16" class="svg octicon-three-bars" aria-hidden="true" width="16" height="16"><path d="M1 2.75A.75.75 0 0 1 1.75 2h12.5a.75.75 0 0 1 0 1.5H1.75A.75.75 0 0 1 1 2.75m0 5A.75.75 0 0 1 1.75 7h12.5a.75.75 0 0 1 0 1.5H1.75A.75.75 0 0 1 1 7.75M1.75 12h12.5a.75.75 0 0 1 0 1.5H1.75a.75.75 0 0 1 0-1.5"/></svg></button>
		</div>

		
		
			<a class="item" href="/explore/repos">Explore</a>
		

		
			<a class="item" target="_blank" href="https://docs.codeberg.org/getting-started/what-is-codeberg/#what-is-codeberg-e.v.%3F">About</a>
			<a class="item" target="_blank" href="https://docs.codeberg.org/getting-started/faq/">FAQ</a>
			<a class="item" target="_blank" rel="noopener noreferrer" href="https://docs.codeberg.org">Help</a>
		

		<a class="item donation-2024" href="https://donate.codeberg.org">Donate 😊🎁🌟
	<style>
		@property --donation-2024-gradient-color-1 {
			syntax: '<color>';
			initial-value: #000;
			inherits: false;
		}

		@property --donation-2024-gradient-color2- {
			syntax: '<color>';
			initial-value: #000;
			inherits: false;
		}
		.donation-2024 {
			--donation-2024-gradient-color-1: var(--color-secondary-alpha-60);
			--donation-2024-gradient-color-2: var(--color-secondary-alpha-60);
			background: linear-gradient(
				to top right,
				var(--donation-2024-gradient-color-1), var(--donation-2024-gradient-color-2)
			) !important;
			transition: --donation-2024-gradient-color-1 250ms, --donation-2024-gradient-color-2 250ms !important;
		}
		.donation-2024:hover {
			--donation-2024-gradient-color-1: var(--color-primary-light-2);
			--donation-2024-gradient-color-2: var(--color-primary-light-1);
		}
	</style>
</a>

	</div>

	
	<div class="navbar-right ui secondary menu">
		
			
				<a class="item" href="/user/cbrgp/CpxzumI">
					<svg viewBox="0 0 16 16" class="svg octicon-person" aria-hidden="true" width="16" height="16"><path d="M10.561 8.073a6 6 0 0 1 3.432 5.142.75.75 0 1 1-1.498.07 4.5 4.5 0 0 0-8.99 0 .75.75 0 0 1-1.498-.07 6 6 0 0 1 3.431-5.142 3.999 3.999 0 1 1 5.123 0M10.5 5a2.5 2.5 0 1 0-5 0 2.5 2.5 0 0 0 5 0"/></svg> Register
				</a>
			
			<a class="item" rel="nofollow" href="/user/login?redirect_to=%2fmister_monster%2fqutebrowser-metascript%2fsrc%2fbranch%2fmaster%2fscript-runner.py">
				<svg viewBox="0 0 16 16" class="svg octicon-sign-in" aria-hidden="true" width="16" height="16"><path d="M2 2.75C2 1.784 2.784 1 3.75 1h2.5a.75.75 0 0 1 0 1.5h-2.5a.25.25 0 0 0-.25.25v10.5c0 .138.112.25.25.25h2.5a.75.75 0 0 1 0 1.5h-2.5A1.75 1.75 0 0 1 2 13.25Zm6.56 4.5h5.69a.75.75 0 0 1 0 1.5H8.56l1.97 1.97a.749.749 0 0 1-.326 1.275.75.75 0 0 1-.734-.215L6.22 8.53a.75.75 0 0 1 0-1.06l3.25-3.25a.749.749 0 0 1 1.275.326.75.75 0 0 1-.215.734Z"/></svg> Sign in
			</a>
		
	</div>
</nav>

		



<div role="main" aria-label="qutebrowser-metascript/script-runner.py at master" class="page-content repository file list ">
	<div class="secondary-nav">

	<div class="ui container">
		<div class="repo-header">
			<div class="flex-item tw-items-center">
				<div class="flex-item-leading">
					

	<svg viewBox="0 0 16 16" class="svg octicon-repo" aria-hidden="true" width="24" height="24"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.5 2.5 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.5 2.5 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.25.25 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg>


				</div>
				<div class="flex-item-main">
					<div class="flex-item-title gt-font-18">
						<a class="muted gt-font-normal" href="/mister_monster">mister_monster</a>/<a class="muted" href="/mister_monster/qutebrowser-metascript">qutebrowser-metascript</a>
					</div>
				</div>
				<div class="flex-item-trailing">
					
					
						
					
					
					
				</div>
			</div>
			
				<div class="repo-buttons button-row">
					
					
					
					
					<a class="ui compact small basic button" href="/mister_monster/qutebrowser-metascript.rss" data-tooltip-content="RSS feed">
						<svg viewBox="0 0 16 16" class="svg octicon-rss" aria-hidden="true" width="16" height="16"><path d="M2.002 2.725a.75.75 0 0 1 .797-.699C8.79 2.42 13.58 7.21 13.974 13.201a.75.75 0 0 1-1.497.098 10.5 10.5 0 0 0-9.776-9.776.747.747 0 0 1-.7-.798ZM2.84 7.05h-.002a7 7 0 0 1 6.113 6.111.75.75 0 0 1-1.49.178 5.5 5.5 0 0 0-4.8-4.8.75.75 0 0 1 .179-1.489M2 13a1 1 0 1 1 2 0 1 1 0 0 1-2 0"/></svg>
					</a>
					
					<form hx-boost="true" hx-target="this" method="post" action="/mister_monster/qutebrowser-metascript/action/watch">
	<div class="ui labeled button" data-tooltip-content="Sign in to watch this repository.">
		<button type="submit" class="ui compact small basic button" disabled>
			
				<svg viewBox="0 0 16 16" class="svg octicon-eye" aria-hidden="true" width="16" height="16"><path d="M8 2c1.981 0 3.671.992 4.933 2.078 1.27 1.091 2.187 2.345 2.637 3.023a1.62 1.62 0 0 1 0 1.798c-.45.678-1.367 1.932-2.637 3.023C11.67 13.008 9.981 14 8 14s-3.671-.992-4.933-2.078C1.797 10.83.88 9.576.43 8.898a1.62 1.62 0 0 1 0-1.798c.45-.677 1.367-1.931 2.637-3.022C4.33 2.992 6.019 2 8 2M1.679 7.932a.12.12 0 0 0 0 .136c.411.622 1.241 1.75 2.366 2.717C5.176 11.758 6.527 12.5 8 12.5s2.825-.742 3.955-1.715c1.124-.967 1.954-2.096 2.366-2.717a.12.12 0 0 0 0-.136c-.412-.621-1.242-1.75-2.366-2.717C10.824 4.242 9.473 3.5 8 3.5s-2.825.742-3.955 1.715c-1.124.967-1.954 2.096-2.366 2.717M8 10a2 2 0 1 1-.001-3.999A2 2 0 0 1 8 10"/></svg><span class="text not-mobile">Watch</span>
			
		</button>
		<a hx-boost="false" class="ui basic label" href="/mister_monster/qutebrowser-metascript/watchers">
			1
		</a>
	</div>
</form>

					
					<form hx-boost="true" hx-target="this" method="post" action="/mister_monster/qutebrowser-metascript/action/star">
	<div class="ui labeled button" data-tooltip-content="Sign in to star this repository.">
		<button type="submit" class="ui compact small basic button" disabled>
			
				<svg viewBox="0 0 16 16" class="svg octicon-star" aria-hidden="true" width="16" height="16"><path d="M8 .25a.75.75 0 0 1 .673.418l1.882 3.815 4.21.612a.75.75 0 0 1 .416 1.279l-3.046 2.97.719 4.192a.751.751 0 0 1-1.088.791L8 12.347l-3.766 1.98a.75.75 0 0 1-1.088-.79l.72-4.194L.818 6.374a.75.75 0 0 1 .416-1.28l4.21-.611L7.327.668A.75.75 0 0 1 8 .25m0 2.445L6.615 5.5a.75.75 0 0 1-.564.41l-3.097.45 2.24 2.184a.75.75 0 0 1 .216.664l-.528 3.084 2.769-1.456a.75.75 0 0 1 .698 0l2.77 1.456-.53-3.084a.75.75 0 0 1 .216-.664l2.24-2.183-3.096-.45a.75.75 0 0 1-.564-.41z"/></svg><span class="text not-mobile">Star</span>
			
		</button>
		<a hx-boost="false" class="ui basic label" href="/mister_monster/qutebrowser-metascript/stars">
			0
		</a>
	</div>
</form>

					
					
					

	<div class="ui labeled button
		
			disabled
		"
		
			data-tooltip-content="Sign in to fork this repository."
		
	>
		<a class="ui compact small basic button"
			
				
			
		>
			<svg viewBox="0 0 16 16" class="svg octicon-repo-forked" aria-hidden="true" width="16" height="16"><path d="M5 5.372v.878c0 .414.336.75.75.75h4.5a.75.75 0 0 0 .75-.75v-.878a2.25 2.25 0 1 1 1.5 0v.878a2.25 2.25 0 0 1-2.25 2.25h-1.5v2.128a2.251 2.251 0 1 1-1.5 0V8.5h-1.5A2.25 2.25 0 0 1 3.5 6.25v-.878a2.25 2.25 0 1 1 1.5 0M5 3.25a.75.75 0 1 0-1.5 0 .75.75 0 0 0 1.5 0m6.75.75a.75.75 0 1 0 0-1.5.75.75 0 0 0 0 1.5m-3 8.75a.75.75 0 1 0-1.5 0 .75.75 0 0 0 1.5 0"/></svg><span class="text not-mobile">Fork</span>
		</a>
		<div class="ui small modal" id="fork-repo-modal">
			<div class="header">
				You've already forked qutebrowser-metascript
			</div>
			<div class="content tw-text-left">
				<div class="ui list">
					
				</div>
				
			</div>
		</div>
		<a class="ui basic label" href="/mister_monster/qutebrowser-metascript/forks">
			0
		</a>
	</div>



					
				</div>
			
		</div>
		
		
		
	</div>

	<overflow-menu class="ui container secondary pointing tabular top attached borderless menu tw-pt-0 tw-my-0">
		
			<div class="overflow-menu-items">
				
					<a class="active item" href="/mister_monster/qutebrowser-metascript">
						<svg viewBox="0 0 16 16" class="svg octicon-code" aria-hidden="true" width="16" height="16"><path d="m11.28 3.22 4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.275-.326.75.75 0 0 1 .215-.734L13.94 8l-3.72-3.72a.749.749 0 0 1 .326-1.275.75.75 0 0 1 .734.215m-6.56 0a.75.75 0 0 1 1.042.018.75.75 0 0 1 .018 1.042L2.06 8l3.72 3.72a.749.749 0 0 1-.326 1.275.75.75 0 0 1-.734-.215L.47 8.53a.75.75 0 0 1 0-1.06Z"/></svg> Code
					</a>
				

				
					<a class="item" href="/mister_monster/qutebrowser-metascript/issues">
						<svg viewBox="0 0 16 16" class="svg octicon-issue-opened" aria-hidden="true" width="16" height="16"><path d="M8 9.5a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3"/><path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0M1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0"/></svg> Issues
						
					</a>
				

				

				
					<a class="item" href="/mister_monster/qutebrowser-metascript/pulls">
						<svg viewBox="0 0 16 16" class="svg octicon-git-pull-request" aria-hidden="true" width="16" height="16"><path d="M1.5 3.25a2.25 2.25 0 1 1 3 2.122v5.256a2.251 2.251 0 1 1-1.5 0V5.372A2.25 2.25 0 0 1 1.5 3.25m5.677-.177L9.573.677A.25.25 0 0 1 10 .854V2.5h1A2.5 2.5 0 0 1 13.5 5v5.628a2.251 2.251 0 1 1-1.5 0V5a1 1 0 0 0-1-1h-1v1.646a.25.25 0 0 1-.427.177L7.177 3.427a.25.25 0 0 1 0-.354M3.75 2.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5m0 9.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5m8.25.75a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0"/></svg> Pull requests
						
					</a>
				

				
					<a href="/mister_monster/qutebrowser-metascript/projects" class="item">
						<svg viewBox="0 0 16 16" class="svg octicon-project" aria-hidden="true" width="16" height="16"><path d="M1.75 0h12.5C15.216 0 16 .784 16 1.75v12.5A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25V1.75C0 .784.784 0 1.75 0M1.5 1.75v12.5c0 .138.112.25.25.25h12.5a.25.25 0 0 0 .25-.25V1.75a.25.25 0 0 0-.25-.25H1.75a.25.25 0 0 0-.25.25M11.75 3a.75.75 0 0 1 .75.75v7.5a.75.75 0 0 1-1.5 0v-7.5a.75.75 0 0 1 .75-.75m-8.25.75a.75.75 0 0 1 1.5 0v5.5a.75.75 0 0 1-1.5 0ZM8 3a.75.75 0 0 1 .75.75v3.5a.75.75 0 0 1-1.5 0v-3.5A.75.75 0 0 1 8 3"/></svg> Projects
						
					</a>
				

				
					<a class="item" href="/mister_monster/qutebrowser-metascript/releases">
						<svg viewBox="0 0 16 16" class="svg octicon-tag" aria-hidden="true" width="16" height="16"><path d="M1 7.775V2.75C1 1.784 1.784 1 2.75 1h5.025c.464 0 .91.184 1.238.513l6.25 6.25a1.75 1.75 0 0 1 0 2.474l-5.026 5.026a1.75 1.75 0 0 1-2.474 0l-6.25-6.25A1.75 1.75 0 0 1 1 7.775m1.5 0c0 .066.026.13.073.177l6.25 6.25a.25.25 0 0 0 .354 0l5.025-5.025a.25.25 0 0 0 0-.354l-6.25-6.25a.25.25 0 0 0-.177-.073H2.75a.25.25 0 0 0-.25.25ZM6 5a1 1 0 1 1 0 2 1 1 0 0 1 0-2"/></svg> Releases
						
					</a>
				

				
					<a href="/mister_monster/qutebrowser-metascript/packages" class="item">
						<svg viewBox="0 0 16 16" class="svg octicon-package" aria-hidden="true" width="16" height="16"><path d="m8.878.392 5.25 3.045c.54.314.872.89.872 1.514v6.098a1.75 1.75 0 0 1-.872 1.514l-5.25 3.045a1.75 1.75 0 0 1-1.756 0l-5.25-3.045A1.75 1.75 0 0 1 1 11.049V4.951c0-.624.332-1.201.872-1.514L7.122.392a1.75 1.75 0 0 1 1.756 0M7.875 1.69l-4.63 2.685L8 7.133l4.755-2.758-4.63-2.685a.25.25 0 0 0-.25 0M2.5 5.677v5.372c0 .09.047.171.125.216l4.625 2.683V8.432Zm6.25 8.271 4.625-2.683a.25.25 0 0 0 .125-.216V5.677L8.75 8.432Z"/></svg> Packages
						
					</a>
				

				
					<a class="item" href="/mister_monster/qutebrowser-metascript/wiki">
						<svg viewBox="0 0 16 16" class="svg octicon-book" aria-hidden="true" width="16" height="16"><path d="M0 1.75A.75.75 0 0 1 .75 1h4.253c1.227 0 2.317.59 3 1.501A3.74 3.74 0 0 1 11.006 1h4.245a.75.75 0 0 1 .75.75v10.5a.75.75 0 0 1-.75.75h-4.507a2.25 2.25 0 0 0-1.591.659l-.622.621a.75.75 0 0 1-1.06 0l-.622-.621A2.25 2.25 0 0 0 5.258 13H.75a.75.75 0 0 1-.75-.75Zm7.251 10.324.004-5.073-.002-2.253A2.25 2.25 0 0 0 5.003 2.5H1.5v9h3.757a3.75 3.75 0 0 1 1.994.574M8.755 4.75l-.004 7.322a3.75 3.75 0 0 1 1.992-.572H14.5v-9h-3.495a2.25 2.25 0 0 0-2.25 2.25"/></svg> Wiki
					</a>
				

				

				
					<a class="item" href="/mister_monster/qutebrowser-metascript/activity">
						<svg viewBox="0 0 16 16" class="svg octicon-pulse" aria-hidden="true" width="16" height="16"><path d="M6 2c.306 0 .582.187.696.471L10 10.731l1.304-3.26A.75.75 0 0 1 12 7h3.25a.75.75 0 0 1 0 1.5h-2.742l-1.812 4.528a.751.751 0 0 1-1.392 0L6 4.77 4.696 8.03A.75.75 0 0 1 4 8.5H.75a.75.75 0 0 1 0-1.5h2.742l1.812-4.529A.75.75 0 0 1 6 2"/></svg> Activity
					</a>
				

				

				

				

				
			</div>
		
	</overflow-menu>
	<div class="ui tabs divider"></div>
</div>

	<div class="ui container ">
		




	<div id="flash-message" hx-swap-oob="true"></div>


		

		
		

		
		










		
		

		
		
		
		<div class="repo-button-row">
			<div class="tw-flex tw-items-center tw-gap-y-2">
				






	




<script type="module">
	const data = {
		'textReleaseCompare': "Compare",
		'textCreateTag': "Create tag %s",
		'textCreateBranch': "Create branch %s",
		'textCreateBranchFrom': "from \"%s\"",
		'textBranches': "Branches",
		'textTags': "Tags",
		'textDefaultBranchLabel': "default",

		'mode': 'branches',
		'showBranchesInDropdown':  true ,
		'searchFieldPlaceholder': 'Filter branch or tag...',
		'branchForm':  null ,
		'disableCreateBranch':  true ,
		'setAction':  null ,
		'submitForm':  null ,
		'viewType': "branch",
		'refName': "master",
		'commitIdShort': "1b5de0789f",
		'tagName': "",
		'branchName': "master",
		'noTag':  null ,
		'defaultSelectedRefName': "master",
		'repoDefaultBranch': "master",
		'enableFeed':  true ,
		'rssURLPrefix': '\/mister_monster\/qutebrowser-metascript/rss/branch/',
		'branchURLPrefix': '\/mister_monster\/qutebrowser-metascript/src/branch/',
		'branchURLSuffix': '/script-runner.py',
		'tagURLPrefix': '\/mister_monster\/qutebrowser-metascript/src/tag/',
		'tagURLSuffix': '/script-runner.py',
		'repoLink': "/mister_monster/qutebrowser-metascript",
		'treePath': "script-runner.py",
		'branchNameSubURL': "branch/master",
		'noResults': "No results found.",
	};
	
	window.config.pageData.branchDropdownDataList = window.config.pageData.branchDropdownDataList || [];
	window.config.pageData.branchDropdownDataList.push(data);
</script>

<div class="js-branch-tag-selector tw-mr-1">
	
	<div class="ui dropdown custom">
		<button class="branch-dropdown-button gt-ellipsis ui basic small compact button tw-flex tw-m-0">
			<span class="text tw-flex tw-items-center tw-mr-1 gt-ellipsis">
				
					
						<svg viewBox="0 0 16 16" class="svg octicon-git-branch" aria-hidden="true" width="16" height="16"><path d="M9.5 3.25a2.25 2.25 0 1 1 3 2.122V6A2.5 2.5 0 0 1 10 8.5H6a1 1 0 0 0-1 1v1.128a2.251 2.251 0 1 1-1.5 0V5.372a2.25 2.25 0 1 1 1.5 0v1.836A2.5 2.5 0 0 1 6 7h4a1 1 0 0 0 1-1v-.628A2.25 2.25 0 0 1 9.5 3.25m-6 0a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0m8.25-.75a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5M4.25 12a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5"/></svg>
					
					<strong ref="dropdownRefName" class="tw-ml-2 tw-inline-block gt-ellipsis">master</strong>
				
			</span>
			<svg viewBox="0 0 16 16" class="dropdown icon svg octicon-triangle-down" aria-hidden="true" width="14" height="14"><path d="m4.427 7.427 3.396 3.396a.25.25 0 0 0 .354 0l3.396-3.396A.25.25 0 0 0 11.396 7H4.604a.25.25 0 0 0-.177.427"/></svg>
		</button>
	</div>
</div>

				
					
					
					
					
					<a id="new-pull-request" role="button" class="ui compact basic button" href="/mister_monster/qutebrowser-metascript/compare/master...master"
						data-tooltip-content="Compare">
						<svg viewBox="0 0 16 16" class="svg octicon-git-pull-request" aria-hidden="true" width="16" height="16"><path d="M1.5 3.25a2.25 2.25 0 1 1 3 2.122v5.256a2.251 2.251 0 1 1-1.5 0V5.372A2.25 2.25 0 0 1 1.5 3.25m5.677-.177L9.573.677A.25.25 0 0 1 10 .854V2.5h1A2.5 2.5 0 0 1 13.5 5v5.628a2.251 2.251 0 1 1-1.5 0V5a1 1 0 0 0-1-1h-1v1.646a.25.25 0 0 1-.427.177L7.177 3.427a.25.25 0 0 1 0-.354M3.75 2.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5m0 9.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5m8.25.75a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0"/></svg>
					</a>
				
				
				

				

				
				
					<span class="breadcrumb repo-path tw-ml-1">
						<a class="section" href="/mister_monster/qutebrowser-metascript/src/branch/master" title="qutebrowser-metascript">qutebrowser-metascript</a><span class="breadcrumb-divider">/</span><span class="active section" title="script-runner.py">script-runner.py</span></span>
				
			</div>
			<div class="tw-flex tw-items-center">
				
				
				
			</div>
		</div>
		
			<div class="tab-size-4 non-diff-file-content">

	
		<div id="repo-file-commit-box" class="ui segment list-header tw-mb-4 tw-flex tw-justify-between">
			<div class="latest-commit">
				
	
		<img loading="lazy" class="ui avatar tw-align-middle tw-mr-2" src="/avatars/22d4d12a0a0deaaeb4d611106ffdac8e?size=48" title="mister monster" width="24" height="24"/>
		
			<a class="muted author-wrapper" title="Mister Monster" href="/mister_monster"><strong>Mister Monster</strong></a>
		
	
	<a rel="nofollow" class="ui sha label " href="/mister_monster/qutebrowser-metascript/commit/e91dbeb03ddef5eb879d0e09ecd09f4adce0fe66">
		<span class="shortsha">e91dbeb03d</span>
		
	</a>
	

	
	<span class="grey commit-summary" title="Upload files to &#39;&#39;"><span class="message-wrapper"><a href="/mister_monster/qutebrowser-metascript/commit/e91dbeb03ddef5eb879d0e09ecd09f4adce0fe66" class="default-link muted">Upload files to &#39;&#39;</a></span>
		
	</span>


			</div>
			
				
					<div class="text grey age">
						<relative-time prefix="" tense="past" datetime="2022-10-19T01:16:04+02:00" data-tooltip-content data-tooltip-interactive="true">2022-10-19 01:16:04 +02:00</relative-time>
					</div>
				
			
		</div>
	

	<h4 class="file-header ui top attached header tw-flex tw-items-center tw-justify-between tw-flex-wrap">
		<div class="file-header-left tw-flex tw-items-center tw-py-2 tw-pr-4">
			
				<div class="file-info tw-font-mono">
	
	
		<div class="file-info-entry">
			56 lines
		</div>
	
	
		<div class="file-info-entry" data-tooltip-content="This file doesn&#39;t contain a trailing end of line character.">
			No EOL
		</div>
	
	
		<div class="file-info-entry">
			1.5 KiB
		</div>
	
	
	
		<div class="file-info-entry">
			Python
		</div>
	
	
	
	
	
</div>

			
		</div>
		<div class="file-header-right file-actions tw-flex tw-items-center tw-flex-wrap">
			
			
				<div class="ui buttons tw-mr-1">
					
					<a class="ui mini basic button" href="/mister_monster/qutebrowser-metascript/raw/branch/master/script-runner.py">Raw</a>
					
						<a class="ui mini basic button" href="/mister_monster/qutebrowser-metascript/src/commit/1b5de0789fe348afa7068ad352fb8be34590b94c/script-runner.py">Permalink</a>
					
					
						<a class="ui mini basic button" href="/mister_monster/qutebrowser-metascript/blame/branch/master/script-runner.py">Blame</a>
					
					<a class="ui mini basic button" href="/mister_monster/qutebrowser-metascript/commits/branch/master/script-runner.py">History</a>
					
				</div>
				<a download href="/mister_monster/qutebrowser-metascript/raw/branch/master/script-runner.py"><span class="btn-octicon" data-tooltip-content="Download file"><svg viewBox="0 0 16 16" class="svg octicon-download" aria-hidden="true" width="16" height="16"><path d="M2.75 14A1.75 1.75 0 0 1 1 12.25v-2.5a.75.75 0 0 1 1.5 0v2.5c0 .138.112.25.25.25h10.5a.25.25 0 0 0 .25-.25v-2.5a.75.75 0 0 1 1.5 0v2.5A1.75 1.75 0 0 1 13.25 14Z"/><path d="M7.25 7.689V2a.75.75 0 0 1 1.5 0v5.689l1.97-1.969a.749.749 0 1 1 1.06 1.06l-3.25 3.25a.75.75 0 0 1-1.06 0L4.22 6.78a.749.749 0 1 1 1.06-1.06z"/></svg></span></a>
				<a href="#" id="copy-content" class="btn-octicon " data-tooltip-content="Copy content"><svg viewBox="0 0 16 16" class="svg octicon-copy" aria-hidden="true" width="14" height="14"><path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"/><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"/></svg></a>
				
					
						<a class="btn-octicon" href="/mister_monster/qutebrowser-metascript/rss/branch/master/script-runner.py" data-tooltip-content="RSS feed">
							<svg viewBox="0 0 16 16" class="svg octicon-rss" aria-hidden="true" width="14" height="14"><path d="M2.002 2.725a.75.75 0 0 1 .797-.699C8.79 2.42 13.58 7.21 13.974 13.201a.75.75 0 0 1-1.497.098 10.5 10.5 0 0 0-9.776-9.776.747.747 0 0 1-.7-.798ZM2.84 7.05h-.002a7 7 0 0 1 6.113 6.111.75.75 0 0 1-1.49.178 5.5 5.5 0 0 0-4.8-4.8.75.75 0 0 1 .179-1.489M2 13a1 1 0 1 1 2 0 1 1 0 0 1-2 0"/></svg>
						</a>
					
				
				
					
						<span class="btn-octicon disabled" data-tooltip-content="You must fork this repository to make or propose changes to this file."><svg viewBox="0 0 16 16" class="svg octicon-pencil" aria-hidden="true" width="16" height="16"><path d="M11.013 1.427a1.75 1.75 0 0 1 2.474 0l1.086 1.086a1.75 1.75 0 0 1 0 2.474l-8.61 8.61c-.21.21-.47.364-.756.445l-3.251.93a.75.75 0 0 1-.927-.928l.929-3.25c.081-.286.235-.547.445-.758l8.61-8.61Zm.176 4.823L9.75 4.81l-6.286 6.287a.25.25 0 0 0-.064.108l-.558 1.953 1.953-.558a.25.25 0 0 0 .108-.064Zm1.238-3.763a.25.25 0 0 0-.354 0L10.811 3.75l1.439 1.44 1.263-1.263a.25.25 0 0 0 0-.354Z"/></svg></span>
					
					
						<span class="btn-octicon disabled" data-tooltip-content="You must have write access to make or propose changes to this file."><svg viewBox="0 0 16 16" class="svg octicon-trash" aria-hidden="true" width="16" height="16"><path d="M11 1.75V3h2.25a.75.75 0 0 1 0 1.5H2.75a.75.75 0 0 1 0-1.5H5V1.75C5 .784 5.784 0 6.75 0h2.5C10.216 0 11 .784 11 1.75M4.496 6.675l.66 6.6a.25.25 0 0 0 .249.225h5.19a.25.25 0 0 0 .249-.225l.66-6.6a.75.75 0 0 1 1.492.149l-.66 6.6A1.75 1.75 0 0 1 10.595 15h-5.19a1.75 1.75 0 0 1-1.741-1.575l-.66-6.6a.75.75 0 1 1 1.492-.15M6.5 1.75V3h3V1.75a.25.25 0 0 0-.25-.25h-2.5a.25.25 0 0 0-.25.25"/></svg></span>
					
				
			
			
		</div>
	</h4>
	<div class="ui bottom attached table unstackable segment">
		
			
	


		
		<div class="file-view code-view">
			
				
				<table>
					<tbody>
						
						
						<tr>
							<td id="L1" class="lines-num"><span id="L1" data-line-number="1"></span></td>
							
							<td rel="L1" class="lines-code chroma"><code class="code-inner"><span class="ch">#!/usr/bin/python3</span>
</code></td>
						</tr>
						
						
						<tr>
							<td id="L2" class="lines-num"><span id="L2" data-line-number="2"></span></td>
							
							<td rel="L2" class="lines-code chroma"><code class="code-inner">
</code></td>
						</tr>
						
						
						<tr>
							<td id="L3" class="lines-num"><span id="L3" data-line-number="3"></span></td>
							
							<td rel="L3" class="lines-code chroma"><code class="code-inner"><span class="kn">from</span> <span class="nn">os</span> <span class="kn">import</span> <span class="n">environ</span> <span class="k">as</span> <span class="n">environ</span>
</code></td>
						</tr>
						
						
						<tr>
							<td id="L4" class="lines-num"><span id="L4" data-line-number="4"></span></td>
							
							<td rel="L4" class="lines-code chroma"><code class="code-inner"><span class="kn">from</span> <span class="nn">time</span> <span class="kn">import</span> <span class="n">sleep</span> <span class="k">as</span> <span class="n">sleep</span>
</code></td>
						</tr>
						
						
						<tr>
							<td id="L5" class="lines-num"><span id="L5" data-line-number="5"></span></td>
							
							<td rel="L5" class="lines-code chroma"><code class="code-inner"><span class="kn">from</span> <span class="nn">sys</span> <span class="kn">import</span> <span class="n">argv</span> <span class="k">as</span> <span class="n">argv</span>
</code></td>
						</tr>
						
						
						<tr>
							<td id="L6" class="lines-num"><span id="L6" data-line-number="6"></span></td>
							
							<td rel="L6" class="lines-code chroma"><code class="code-inner">
</code></td>
						</tr>
						
						
						<tr>
							<td id="L7" class="lines-num"><span id="L7" data-line-number="7"></span></td>
							
							<td rel="L7" class="lines-code chroma"><code class="code-inner"><span class="c1"># run a qutebrowser command</span>
</code></td>
						</tr>
						
						
						<tr>
							<td id="L8" class="lines-num"><span id="L8" data-line-number="8"></span></td>
							
							<td rel="L8" class="lines-code chroma"><code class="code-inner"><span class="k">def</span> <span class="nf">run_qb_command</span><span class="p">(</span><span class="n">command</span><span class="p">)</span><span class="p">:</span>
</code></td>
						</tr>
						
						
						<tr>
							<td id="L9" class="lines-num"><span id="L9" data-line-number="9"></span></td>
							
							<td rel="L9" class="lines-code chroma"><code class="code-inner">    <span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="n">environ</span><span class="p">[</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">QUTE_FIFO</span><span class="s2">&#34;</span><span class="p">]</span><span class="p">,</span> <span class="sa"></span><span class="s2">&#34;</span><span class="s2">a</span><span class="s2">&#34;</span><span class="p">)</span> <span class="k">as</span> <span class="n">output</span><span class="p">:</span>
</code></td>
						</tr>
						
						
						<tr>
							<td id="L10" class="lines-num"><span id="L10" data-line-number="10"></span></td>
							
							<td rel="L10" class="lines-code chroma"><code class="code-inner">        <span class="n">output</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">command</span><span class="p">)</span>
</code></td>
						</tr>
						
						
						<tr>
							<td id="L11" class="lines-num"><span id="L11" data-line-number="11"></span></td>
							
							<td rel="L11" class="lines-code chroma"><code class="code-inner">    <span class="n">sleep</span><span class="p">(</span><span class="n">wait_time</span><span class="p">)</span>
</code></td>
						</tr>
						
						
						<tr>
							<td id="L12" class="lines-num"><span id="L12" data-line-number="12"></span></td>
							
							<td rel="L12" class="lines-code chroma"><code class="code-inner">
</code></td>
						</tr>
						
						
						<tr>
							<td id="L13" class="lines-num"><span id="L13" data-line-number="13"></span></td>
							
							<td rel="L13" class="lines-code chroma"><code class="code-inner"><span class="c1"># open and read the command script content</span>
</code></td>
						</tr>
						
						
						<tr>
							<td id="L14" class="lines-num"><span id="L14" data-line-number="14"></span></td>
							
							<td rel="L14" class="lines-code chroma"><code class="code-inner"><span class="k">def</span> <span class="nf">read_metascript</span><span class="p">(</span><span class="n">scripts_path</span><span class="p">,</span> <span class="n">script</span><span class="p">)</span><span class="p">:</span>
</code></td>
						</tr>
						
						
						<tr>
							<td id="L15" class="lines-num"><span id="L15" data-line-number="15"></span></td>
							
							<td rel="L15" class="lines-code chroma"><code class="code-inner">    <span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="n">scripts_path</span> <span class="o">+</span> <span class="n">script</span><span class="p">,</span> <span class="sa"></span><span class="s2">&#34;</span><span class="s2">r</span><span class="s2">&#34;</span><span class="p">)</span> <span class="k">as</span> <span class="n">script_file</span><span class="p">:</span>
</code></td>
						</tr>
						
						
						<tr>
							<td id="L16" class="lines-num"><span id="L16" data-line-number="16"></span></td>
							
							<td rel="L16" class="lines-code chroma"><code class="code-inner">        <span class="n">script_content</span> <span class="o">=</span> <span class="n">script_file</span><span class="o">.</span><span class="n">read</span><span class="p">(</span><span class="p">)</span>
</code></td>
						</tr>
						
						
						<tr>
							<td id="L17" class="lines-num"><span id="L17" data-line-number="17"></span></td>
							
							<td rel="L17" class="lines-code chroma"><code class="code-inner">    <span class="k">return</span> <span class="n">script_content</span>
</code></td>
						</tr>
						
						
						<tr>
							<td id="L18" class="lines-num"><span id="L18" data-line-number="18"></span></td>
							
							<td rel="L18" class="lines-code chroma"><code class="code-inner">
</code></td>
						</tr>
						
						
						<tr>
							<td id="L19" class="lines-num"><span id="L19" data-line-number="19"></span></td>
							
							<td rel="L19" class="lines-code chroma"><code class="code-inner"><span class="c1"># parse script content to get only the commands</span>
</code></td>
						</tr>
						
						
						<tr>
							<td id="L20" class="lines-num"><span id="L20" data-line-number="20"></span></td>
							
							<td rel="L20" class="lines-code chroma"><code class="code-inner"><span class="k">def</span> <span class="nf">parse_metascript</span><span class="p">(</span><span class="n">script_content</span><span class="p">)</span><span class="p">:</span>
</code></td>
						</tr>
						
						
						<tr>
							<td id="L21" class="lines-num"><span id="L21" data-line-number="21"></span></td>
							
							<td rel="L21" class="lines-code chroma"><code class="code-inner">    <span class="n">commands_list</span> <span class="o">=</span> <span class="p">[</span><span class="p">]</span>
</code></td>
						</tr>
						
						
						<tr>
							<td id="L22" class="lines-num"><span id="L22" data-line-number="22"></span></td>
							
							<td rel="L22" class="lines-code chroma"><code class="code-inner">    <span class="k">for</span> <span class="n">line</span> <span class="ow">in</span> <span class="n">script_content</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="sa"></span><span class="s2">&#34;</span><span class="se">\n</span><span class="s2">&#34;</span><span class="p">)</span><span class="p">:</span>
</code></td>
						</tr>
						
						
						<tr>
							<td id="L23" class="lines-num"><span id="L23" data-line-number="23"></span></td>
							
							<td rel="L23" class="lines-code chroma"><code class="code-inner">        <span class="k">if</span> <span class="n">line</span> <span class="o">==</span> <span class="sa"></span><span class="s2">&#34;</span><span class="s2">&#34;</span><span class="p">:</span>
</code></td>
						</tr>
						
						
						<tr>
							<td id="L24" class="lines-num"><span id="L24" data-line-number="24"></span></td>
							
							<td rel="L24" class="lines-code chroma"><code class="code-inner">            <span class="k">pass</span>
</code></td>
						</tr>
						
						
						<tr>
							<td id="L25" class="lines-num"><span id="L25" data-line-number="25"></span></td>
							
							<td rel="L25" class="lines-code chroma"><code class="code-inner">        <span class="k">elif</span> <span class="n">line</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">==</span> <span class="sa"></span><span class="s2">&#34;</span><span class="s2">#</span><span class="s2">&#34;</span><span class="p">:</span>
</code></td>
						</tr>
						
						
						<tr>
							<td id="L26" class="lines-num"><span id="L26" data-line-number="26"></span></td>
							
							<td rel="L26" class="lines-code chroma"><code class="code-inner">            <span class="k">pass</span>
</code></td>
						</tr>
						
						
						<tr>
							<td id="L27" class="lines-num"><span id="L27" data-line-number="27"></span></td>
							
							<td rel="L27" class="lines-code chroma"><code class="code-inner">        <span class="k">elif</span> <span class="n">line</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">==</span> <span class="sa"></span><span class="s2">&#34;</span><span class="s2">:</span><span class="s2">&#34;</span><span class="p">:</span>
</code></td>
						</tr>
						
						
						<tr>
							<td id="L28" class="lines-num"><span id="L28" data-line-number="28"></span></td>
							
							<td rel="L28" class="lines-code chroma"><code class="code-inner">            <span class="n">command</span> <span class="o">=</span> <span class="n">line</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">#</span><span class="s2">&#34;</span><span class="p">)</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
</code></td>
						</tr>
						
						
						<tr>
							<td id="L29" class="lines-num"><span id="L29" data-line-number="29"></span></td>
							
							<td rel="L29" class="lines-code chroma"><code class="code-inner">            <span class="n">commands_list</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">command</span><span class="p">)</span>
</code></td>
						</tr>
						
						
						<tr>
							<td id="L30" class="lines-num"><span id="L30" data-line-number="30"></span></td>
							
							<td rel="L30" class="lines-code chroma"><code class="code-inner">        <span class="k">else</span><span class="p">:</span>
</code></td>
						</tr>
						
						
						<tr>
							<td id="L31" class="lines-num"><span id="L31" data-line-number="31"></span></td>
							
							<td rel="L31" class="lines-code chroma"><code class="code-inner">            <span class="k">pass</span>
</code></td>
						</tr>
						
						
						<tr>
							<td id="L32" class="lines-num"><span id="L32" data-line-number="32"></span></td>
							
							<td rel="L32" class="lines-code chroma"><code class="code-inner">    <span class="k">return</span> <span class="n">commands_list</span>
</code></td>
						</tr>
						
						
						<tr>
							<td id="L33" class="lines-num"><span id="L33" data-line-number="33"></span></td>
							
							<td rel="L33" class="lines-code chroma"><code class="code-inner">
</code></td>
						</tr>
						
						
						<tr>
							<td id="L34" class="lines-num"><span id="L34" data-line-number="34"></span></td>
							
							<td rel="L34" class="lines-code chroma"><code class="code-inner"><span class="c1"># replace all variables in a command with corresponding arguments</span>
</code></td>
						</tr>
						
						
						<tr>
							<td id="L35" class="lines-num"><span id="L35" data-line-number="35"></span></td>
							
							<td rel="L35" class="lines-code chroma"><code class="code-inner"><span class="k">def</span> <span class="nf">replace_args</span><span class="p">(</span><span class="n">args</span><span class="p">,</span> <span class="n">command</span><span class="p">)</span><span class="p">:</span>
</code></td>
						</tr>
						
						
						<tr>
							<td id="L36" class="lines-num"><span id="L36" data-line-number="36"></span></td>
							
							<td rel="L36" class="lines-code chroma"><code class="code-inner">    <span class="n">command</span> <span class="o">=</span> <span class="n">command</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="sa"></span><span class="s2">&#34;</span><span class="s2">|</span><span class="s2">&#34;</span><span class="p">)</span>
</code></td>
						</tr>
						
						
						<tr>
							<td id="L37" class="lines-num"><span id="L37" data-line-number="37"></span></td>
							
							<td rel="L37" class="lines-code chroma"><code class="code-inner">    <span class="k">for</span> <span class="n">part</span> <span class="ow">in</span> <span class="n">command</span><span class="p">:</span>
</code></td>
						</tr>
						
						
						<tr>
							<td id="L38" class="lines-num"><span id="L38" data-line-number="38"></span></td>
							
							<td rel="L38" class="lines-code chroma"><code class="code-inner">        <span class="k">try</span><span class="p">:</span>
</code></td>
						</tr>
						
						
						<tr>
							<td id="L39" class="lines-num"><span id="L39" data-line-number="39"></span></td>
							
							<td rel="L39" class="lines-code chroma"><code class="code-inner">            <span class="n">arg_index</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">part</span><span class="p">)</span> <span class="o">-</span> <span class="mi">1</span>
</code></td>
						</tr>
						
						
						<tr>
							<td id="L40" class="lines-num"><span id="L40" data-line-number="40"></span></td>
							
							<td rel="L40" class="lines-code chroma"><code class="code-inner">            <span class="n">command</span><span class="p">[</span><span class="n">command</span><span class="o">.</span><span class="n">index</span><span class="p">(</span><span class="n">part</span><span class="p">)</span><span class="p">]</span> <span class="o">=</span> <span class="n">args</span><span class="p">[</span><span class="n">arg_index</span><span class="p">]</span>
</code></td>
						</tr>
						
						
						<tr>
							<td id="L41" class="lines-num"><span id="L41" data-line-number="41"></span></td>
							
							<td rel="L41" class="lines-code chroma"><code class="code-inner">        <span class="k">except</span><span class="p">:</span>
</code></td>
						</tr>
						
						
						<tr>
							<td id="L42" class="lines-num"><span id="L42" data-line-number="42"></span></td>
							
							<td rel="L42" class="lines-code chroma"><code class="code-inner">            <span class="k">pass</span>
</code></td>
						</tr>
						
						
						<tr>
							<td id="L43" class="lines-num"><span id="L43" data-line-number="43"></span></td>
							
							<td rel="L43" class="lines-code chroma"><code class="code-inner">    <span class="n">command</span> <span class="o">=</span> <span class="sa"></span><span class="s2">&#34;</span><span class="s2">&#34;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">command</span><span class="p">)</span>
</code></td>
						</tr>
						
						
						<tr>
							<td id="L44" class="lines-num"><span id="L44" data-line-number="44"></span></td>
							
							<td rel="L44" class="lines-code chroma"><code class="code-inner">    <span class="k">return</span> <span class="n">command</span>
</code></td>
						</tr>
						
						
						<tr>
							<td id="L45" class="lines-num"><span id="L45" data-line-number="45"></span></td>
							
							<td rel="L45" class="lines-code chroma"><code class="code-inner">
</code></td>
						</tr>
						
						
						<tr>
							<td id="L46" class="lines-num"><span id="L46" data-line-number="46"></span></td>
							
							<td rel="L46" class="lines-code chroma"><code class="code-inner"><span class="k">def</span> <span class="nf">run</span><span class="p">(</span><span class="p">)</span><span class="p">:</span>
</code></td>
						</tr>
						
						
						<tr>
							<td id="L47" class="lines-num"><span id="L47" data-line-number="47"></span></td>
							
							<td rel="L47" class="lines-code chroma"><code class="code-inner">    <span class="n">scripts_path</span> <span class="o">=</span> <span class="n">argv</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span>
</code></td>
						</tr>
						
						
						<tr>
							<td id="L48" class="lines-num"><span id="L48" data-line-number="48"></span></td>
							
							<td rel="L48" class="lines-code chroma"><code class="code-inner">    <span class="n">script</span> <span class="o">=</span> <span class="n">argv</span><span class="p">[</span><span class="mi">2</span><span class="p">]</span>
</code></td>
						</tr>
						
						
						<tr>
							<td id="L49" class="lines-num"><span id="L49" data-line-number="49"></span></td>
							
							<td rel="L49" class="lines-code chroma"><code class="code-inner">    <span class="n">args</span> <span class="o">=</span> <span class="n">argv</span><span class="p">[</span><span class="mi">3</span><span class="p">:</span><span class="p">]</span>
</code></td>
						</tr>
						
						
						<tr>
							<td id="L50" class="lines-num"><span id="L50" data-line-number="50"></span></td>
							
							<td rel="L50" class="lines-code chroma"><code class="code-inner">    <span class="n">commands</span> <span class="o">=</span> <span class="n">parse_metascript</span><span class="p">(</span><span class="n">read_metascript</span><span class="p">(</span><span class="n">scripts_path</span><span class="p">,</span> <span class="n">script</span><span class="p">)</span><span class="p">)</span>
</code></td>
						</tr>
						
						
						<tr>
							<td id="L51" class="lines-num"><span id="L51" data-line-number="51"></span></td>
							
							<td rel="L51" class="lines-code chroma"><code class="code-inner">    <span class="k">for</span> <span class="n">command</span> <span class="ow">in</span> <span class="n">commands</span><span class="p">:</span>
</code></td>
						</tr>
						
						
						<tr>
							<td id="L52" class="lines-num"><span id="L52" data-line-number="52"></span></td>
							
							<td rel="L52" class="lines-code chroma"><code class="code-inner">        <span class="n">command</span> <span class="o">=</span> <span class="n">replace_args</span><span class="p">(</span><span class="n">args</span><span class="p">,</span> <span class="n">command</span><span class="p">)</span>
</code></td>
						</tr>
						
						
						<tr>
							<td id="L53" class="lines-num"><span id="L53" data-line-number="53"></span></td>
							
							<td rel="L53" class="lines-code chroma"><code class="code-inner">        <span class="n">run_qb_command</span><span class="p">(</span><span class="n">command</span><span class="p">)</span>
</code></td>
						</tr>
						
						
						<tr>
							<td id="L54" class="lines-num"><span id="L54" data-line-number="54"></span></td>
							
							<td rel="L54" class="lines-code chroma"><code class="code-inner">
</code></td>
						</tr>
						
						
						<tr>
							<td id="L55" class="lines-num"><span id="L55" data-line-number="55"></span></td>
							
							<td rel="L55" class="lines-code chroma"><code class="code-inner"><span class="n">wait_time</span> <span class="o">=</span> <span class="mf">0.3</span>
</code></td>
						</tr>
						
						
						<tr>
							<td id="L56" class="lines-num"><span id="L56" data-line-number="56"></span></td>
							
							<td rel="L56" class="lines-code chroma"><code class="code-inner"><span class="n">run</span><span class="p">(</span><span class="p">)</span></code></td>
						</tr>
						
					</tbody>
				</table>
				<div class="code-line-menu tippy-target">
					
						<a class="item ref-in-new-issue" role="menuitem" data-url-issue-new="/mister_monster/qutebrowser-metascript/issues/new" data-url-param-body-link="/mister_monster/qutebrowser-metascript/src/commit/1b5de0789fe348afa7068ad352fb8be34590b94c/script-runner.py" rel="nofollow noindex">Reference in a new issue</a>
					
					<a class="item view_git_blame" role="menuitem" href="/mister_monster/qutebrowser-metascript/blame/commit/1b5de0789fe348afa7068ad352fb8be34590b94c/script-runner.py">View git blame</a>
					<a class="item copy-line-permalink" role="menuitem" data-url="/mister_monster/qutebrowser-metascript/src/commit/1b5de0789fe348afa7068ad352fb8be34590b94c/script-runner.py">Copy permalink</a>
				</div>
				
			
		</div>
	</div>
</div>

		
	</div>
</div>


	

	</div>

	

	<footer class="page-footer" role="group" aria-label="Footer">
	<div class="grid" aria-label="Links">
		<div class="branding not-mobile" aria-hidden="true">
			<img src="https://design.codeberg.org/logo-kit/icon_inverted.svg">
		</div>
		<div>
			<b>Codeberg</b>
			<ul>
				<li><a href="https://docs.codeberg.org" target="_blank">Documentation</a></li>
				<li><a href="/Codeberg/Community/issues">Community Issues</a></li>
				
				<li><a href="/Codeberg/Contributing">Contributing</a>
				<li><a href="https://docs.codeberg.org/contact/#abuse" target="_blank">Report Abuse</a>
			</ul>
		</div>
		<div>
			<b>Association</b>
			<ul>
				<li><a href="https://docs.codeberg.org/getting-started/what-is-codeberg/#what-is-codeberg-e.v.%3F" target="_blank">Who are we?</a></li>
				<li><a href="/codeberg/org/src/en/bylaws.md" target="_blank">Bylaws / Satzung</a></li>
				<li><a href="https://docs.codeberg.org/improving-codeberg/donate/" target="_blank">Donate</a></li>
				<li><a href="https://join.codeberg.org" target="_blank">Join / Support</a></li>
				<li><a href="https://docs.codeberg.org/contact/" target="_blank">Contact</a></li>
			</ul>
		</div>
		<div>
			<b>Service</b>
			<ul>
				<li><a href="https://codeberg.page" target="_blank">Codeberg Pages</a></li>
				<li><a href="https://translate.codeberg.org" target="_blank">Weblate Translations</a></li>
				<li><a href="https://docs.codeberg.org/ci/#using-codeberg's-instance-of-woodpecker-ci" target="_blank">Woodpecker CI</a></li>
				
					<li><a href="/api/swagger">Forgejo API</a></li>
				
				<li><a href="https://status.codeberg.eu" target="_blank">Status Page</a></li>
			</ul>
		</div>
		<div>
			<b>Legal</b>
			<ul>
				<li><a href="/codeberg/org/src/Imprint.md" target="_blank">Imprint / Impressum</a></li>
				<li><a href="/codeberg/org/src/PrivacyPolicy.md" target="_blank">Privacy Policy</a></li>
				<li><a href="/assets/licenses.txt">Licenses</a></li>
				<li><a href="/codeberg/org/src/TermsOfUse.md">Terms of Use</a></li>
			</ul>
		</div>
	</div>
	<center>
		<a href="https://blog.codeberg.org" target="_blank">Blog</a> |
		<a href="https://social.anoxinon.de/@Codeberg" target="_blank" rel="noopener noreferrer">Mastodon</a> |
		<a href="https://matrix.to/#/#codeberg-space:matrix.org" target="_blank" rel="noopener noreferrer">Matrix Space</a> |
		<a href="/Codeberg-Infrastructure/forgejo" target="_blank">Powered by Forgejo</a>
	</center>
	<div class="gt-float-right">
		<div class="ui language bottom floating slide up dropdown link item button">
			<svg viewBox="0 0 16 16" class="svg octicon-globe" aria-hidden="true" width="16" height="16"><path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0M5.78 8.75a9.64 9.64 0 0 0 1.363 4.177q.383.64.857 1.215c.245-.296.551-.705.857-1.215A9.64 9.64 0 0 0 10.22 8.75Zm4.44-1.5a9.64 9.64 0 0 0-1.363-4.177c-.307-.51-.612-.919-.857-1.215a10 10 0 0 0-.857 1.215A9.64 9.64 0 0 0 5.78 7.25Zm-5.944 1.5H1.543a6.51 6.51 0 0 0 4.666 5.5q-.184-.271-.352-.552c-.715-1.192-1.437-2.874-1.581-4.948m-2.733-1.5h2.733c.144-2.074.866-3.756 1.58-4.948q.18-.295.353-.552a6.51 6.51 0 0 0-4.666 5.5m10.181 1.5c-.144 2.074-.866 3.756-1.58 4.948q-.18.296-.353.552a6.51 6.51 0 0 0 4.666-5.5Zm2.733-1.5a6.51 6.51 0 0 0-4.666-5.5q.184.272.353.552c.714 1.192 1.436 2.874 1.58 4.948Z"/></svg>
			<div class="text">English</div>
			<div class="menu language-menu">
				
					<a lang="id-ID" data-url="/?lang=id-ID" class="item ">Bahasa Indonesia</a>
				
					<a lang="de-DE" data-url="/?lang=de-DE" class="item ">Deutsch</a>
				
					<a lang="en-US" data-url="/?lang=en-US" class="item active selected">English</a>
				
					<a lang="es-ES" data-url="/?lang=es-ES" class="item ">Español</a>
				
					<a lang="eo" data-url="/?lang=eo" class="item ">Esperanto</a>
				
					<a lang="fil" data-url="/?lang=fil" class="item ">Filipino</a>
				
					<a lang="fr-FR" data-url="/?lang=fr-FR" class="item ">Français</a>
				
					<a lang="it-IT" data-url="/?lang=it-IT" class="item ">Italiano</a>
				
					<a lang="lv-LV" data-url="/?lang=lv-LV" class="item ">Latviešu</a>
				
					<a lang="hu-HU" data-url="/?lang=hu-HU" class="item ">Magyar nyelv</a>
				
					<a lang="nl-NL" data-url="/?lang=nl-NL" class="item ">Nederlands</a>
				
					<a lang="pl-PL" data-url="/?lang=pl-PL" class="item ">Polski</a>
				
					<a lang="pt-PT" data-url="/?lang=pt-PT" class="item ">Português de Portugal</a>
				
					<a lang="pt-BR" data-url="/?lang=pt-BR" class="item ">Português do Brasil</a>
				
					<a lang="sl" data-url="/?lang=sl" class="item ">Slovenščina</a>
				
					<a lang="fi-FI" data-url="/?lang=fi-FI" class="item ">Suomi</a>
				
					<a lang="sv-SE" data-url="/?lang=sv-SE" class="item ">Svenska</a>
				
					<a lang="tr-TR" data-url="/?lang=tr-TR" class="item ">Türkçe</a>
				
					<a lang="cs-CZ" data-url="/?lang=cs-CZ" class="item ">Čeština</a>
				
					<a lang="el-GR" data-url="/?lang=el-GR" class="item ">Ελληνικά</a>
				
					<a lang="bg" data-url="/?lang=bg" class="item ">Български</a>
				
					<a lang="ru-RU" data-url="/?lang=ru-RU" class="item ">Русский</a>
				
					<a lang="uk-UA" data-url="/?lang=uk-UA" class="item ">Українська</a>
				
					<a lang="fa-IR" data-url="/?lang=fa-IR" class="item ">فارسی</a>
				
					<a lang="ja-JP" data-url="/?lang=ja-JP" class="item ">日本語</a>
				
					<a lang="zh-CN" data-url="/?lang=zh-CN" class="item ">简体中文</a>
				
					<a lang="zh-TW" data-url="/?lang=zh-TW" class="item ">繁體中文（台灣）</a>
				
					<a lang="zh-HK" data-url="/?lang=zh-HK" class="item ">繁體中文（香港）</a>
				
					<a lang="ko-KR" data-url="/?lang=ko-KR" class="item ">한국어</a>
				
			</div>
		</div>
	</div>
</footer>


	<script src="/assets/js/index.js?v=9.0.0-226-28dcc7f11a~gitea-1.22.0" onerror="alert('Failed to load asset files from ' + this.src + '. Please make sure the asset files can be accessed.')"></script>

	
</body>
</html>

