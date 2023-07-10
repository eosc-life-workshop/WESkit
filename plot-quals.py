




<!DOCTYPE html>
<html class="with-top-bar " lang="en">
<head prefix="og: http://ogp.me/ns#">
<meta charset="utf-8">
<title>2_cloud/plot-quals.py · master · Sven Twardziok / espace_eucancan_training_snakemake · GitLab</title>
<link rel="preload" href="/assets/application_utilities-1c4ade9c8e773a7f9d6f2590b456e568911240f47b9c79ef708e9344ecb094fe.css" as="style" type="text/css" nonce="zIJO2rDBwF46607vbZydvA==">
<link rel="preload" href="/assets/application-af4ecb7c5c3914e54d68b56aae277727784eca7e78c1fb8ec711e4b53fd90601.css" as="style" type="text/css" nonce="zIJO2rDBwF46607vbZydvA==">
<link rel="preload" href="/assets/highlight/themes/white-8ded44488c9b4c1cbea299cc42721314d16f00a228733ce59c08194a7994a650.css" as="style" type="text/css" nonce="zIJO2rDBwF46607vbZydvA==">
<link crossorigin="" href="https://snowplow.trx.gitlab.net" rel="preconnect">
<link as="font" crossorigin="" href="/assets/gitlab-sans/GitLabSans-1e0a5107ea3bbd4be93e8ad2c503467e43166cd37e4293570b490e0812ede98b.woff2" rel="preload">
<link as="font" crossorigin="" href="/assets/gitlab-mono/GitLabMono-08d2c5e8ff8fd3d2d6ec55bc7713380f8981c35f9d2df14e12b835464d6e8f23.woff2" rel="preload">
<link as="font" crossorigin="" href="/assets/gitlab-mono/GitLabMono-Italic-38e58d8df29485a20c550da1d0111e2c2169f6dcbcf894f2cd3afbdd97bcc588.woff2" rel="preload">
<link rel="preload" href="/assets/fonts-171e1863d044918ea3bbaacf2a559ccaac603904aa851c3add5b714fa7066468.css" as="style" type="text/css" nonce="zIJO2rDBwF46607vbZydvA==">

<meta content="IE=edge" http-equiv="X-UA-Compatible">
<script nonce="JrdoIUEtKppIkHqgKvi9kg==">
//<![CDATA[
var gl = window.gl || {};
gl.startup_calls = null;
gl.startup_graphql_calls = [{"query":"query getBlobInfo(\n  $projectPath: ID!\n  $filePath: String!\n  $ref: String!\n  $shouldFetchRawText: Boolean!\n) {\n  project(fullPath: $projectPath) {\n    __typename\n    id\n    repository {\n      __typename\n      empty\n      blobs(paths: [$filePath], ref: $ref) {\n        __typename\n        nodes {\n          __typename\n          id\n          webPath\n          name\n          size\n          rawSize\n          rawTextBlob @include(if: $shouldFetchRawText)\n          fileType\n          language\n          path\n          blamePath\n          editBlobPath\n          gitpodBlobUrl\n          ideEditPath\n          forkAndEditPath\n          ideForkAndEditPath\n          codeNavigationPath\n          projectBlobPathRoot\n          forkAndViewPath\n          environmentFormattedExternalUrl\n          environmentExternalUrlForRouteMap\n          canModifyBlob\n          canCurrentUserPushToBranch\n          archived\n          storedExternally\n          externalStorage\n          externalStorageUrl\n          rawPath\n          replacePath\n          pipelineEditorPath\n          simpleViewer {\n            fileType\n            tooLarge\n            type\n            renderError\n          }\n          richViewer {\n            fileType\n            tooLarge\n            type\n            renderError\n          }\n        }\n      }\n    }\n  }\n}\n","variables":{"projectPath":"twardzso/espace_eucancan_training_snakemake","ref":"master","filePath":"2_cloud/plot-quals.py","shouldFetchRawText":true}}];

if (gl.startup_calls && window.fetch) {
  Object.keys(gl.startup_calls).forEach(apiCall => {
   gl.startup_calls[apiCall] = {
      fetchCall: fetch(apiCall, {
        // Emulate XHR for Rails AJAX request checks
        headers: {
          'X-Requested-With': 'XMLHttpRequest'
        },
        // fetch won’t send cookies in older browsers, unless you set the credentials init option.
        // We set to `same-origin` which is default value in modern browsers.
        // See https://github.com/whatwg/fetch/pull/585 for more information.
        credentials: 'same-origin'
      })
    };
  });
}
if (gl.startup_graphql_calls && window.fetch) {
  const headers = {"X-CSRF-Token":"8kPwgCJmcRhOTjRgaGmJJ0S6rS3u2qpbo1Hwk3PksqQGFlSq8FJD1HNX23AVr5CerZVfft1tS5yH0ZSuq8NCPg","x-gitlab-feature-category":"source_code_management"};
  const url = `https://gitlab.com/api/graphql`

  const opts = {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      ...headers,
    }
  };

  gl.startup_graphql_calls = gl.startup_graphql_calls.map(call => ({
    ...call,
    fetchCall: fetch(url, {
      ...opts,
      credentials: 'same-origin',
      body: JSON.stringify(call)
    })
  }))
}


//]]>
</script>

<link rel="prefetch" href="/assets/webpack/monaco.b6d98c9f.chunk.js">
<link rel="icon" type="image/png" href="/assets/favicon-72a2cad5025aa931d6ea56c3201d1f18e68a8cd39788c7c80d5b2b82aa5143ef.png" id="favicon" data-original-href="/assets/favicon-72a2cad5025aa931d6ea56c3201d1f18e68a8cd39788c7c80d5b2b82aa5143ef.png" />
<link rel="stylesheet" href="/assets/themes/theme_indigo-3331cd49e4ca5527df9ebb4ec47e8d1463168d5a75df83bf264da79f38af4c96.css" />

<link rel="stylesheet" href="/assets/application-af4ecb7c5c3914e54d68b56aae277727784eca7e78c1fb8ec711e4b53fd90601.css" media="all" />
<link rel="stylesheet" href="/assets/page_bundles/tree-86a16f68ea7bde025a5a521d3a1332e85e8484bad7d4c52e0bd04f0ed1b3571f.css" media="all" />
<link rel="stylesheet" href="/assets/application_utilities-1c4ade9c8e773a7f9d6f2590b456e568911240f47b9c79ef708e9344ecb094fe.css" media="all" />


<link rel="stylesheet" href="/assets/fonts-171e1863d044918ea3bbaacf2a559ccaac603904aa851c3add5b714fa7066468.css" media="all" />
<link rel="stylesheet" href="/assets/highlight/themes/white-8ded44488c9b4c1cbea299cc42721314d16f00a228733ce59c08194a7994a650.css" media="all" />

<script src="/assets/webpack/runtime.f0316be3.bundle.js" defer="defer" nonce="JrdoIUEtKppIkHqgKvi9kg=="></script>
<script src="/assets/webpack/main.758ff064.chunk.js" defer="defer" nonce="JrdoIUEtKppIkHqgKvi9kg=="></script>
<script src="/assets/webpack/tracker.3491b11b.chunk.js" defer="defer" nonce="JrdoIUEtKppIkHqgKvi9kg=="></script>
<script nonce="JrdoIUEtKppIkHqgKvi9kg==">
//<![CDATA[
window.snowplowOptions = {"namespace":"gl","hostname":"snowplow.trx.gitlab.net","cookieDomain":".gitlab.com","appId":"gitlab","formTracking":true,"linkClickTracking":true}

gl = window.gl || {};
gl.snowplowStandardContext = {"schema":"iglu:com.gitlab/gitlab_standard/jsonschema/1-0-9","data":{"environment":"production","source":"gitlab-rails","plan":"free","extra":{"new_nav":true},"user_id":9541565,"namespace_id":5500677,"project_id":23446064,"context_generated_at":"2023-07-10T12:18:16.961Z"}}
gl.snowplowPseudonymizedPageUrl = "https://gitlab.com/namespace5500677/project23446064/-/blob/:repository_path";


//]]>
</script>
<script nonce="JrdoIUEtKppIkHqgKvi9kg==">
//<![CDATA[
window.gon={};gon.api_version="v4";gon.default_avatar_url="https://gitlab.com/assets/no_avatar-849f9c04a3a0d0cea2424ae97b27447dc64a7dbfae83c036c45b403392f0e8ba.png";gon.max_file_size=100;gon.asset_host=null;gon.webpack_public_path="/assets/webpack/";gon.relative_url_root="";gon.user_color_scheme="white";gon.markdown_surround_selection=true;gon.markdown_automatic_lists=true;gon.sentry_dsn="https://f5573e26de8f4293b285e556c35dfd6e@new-sentry.gitlab.net/4";gon.sentry_environment="gprd";gon.recaptcha_api_server_url="https://www.recaptcha.net/recaptcha/api.js";gon.recaptcha_sitekey="6LfAERQTAAAAAL4GYSiAMGLbcLyUIBSfPrDNJgeC";gon.gitlab_url="https://gitlab.com";gon.revision="e124cf77951";gon.feature_category="source_code_management";gon.gitlab_logo="/assets/gitlab_logo-2957169c8ef64c58616a1ac3f4fc626e8a35ce4eb3ed31bb0d873712f2a041a0.png";gon.secure=true;gon.sprite_icons="/assets/icons-b8c5a9711f73b1de3c81754da0aca72f43b0e6844aa06dd03092b601a493f45b.svg";gon.sprite_file_icons="/assets/file_icons/file_icons-6489590d770258cc27e4698405d309d83e42829b667b4d601534321e96739a5a.svg";gon.emoji_sprites_css_path="/assets/emoji_sprites-e1b1ba2d7a86a445dcb1110d1b6e7dd0200ecaa993a445df77a07537dbf8f475.css";gon.gridstack_css_path="/assets/lazy_bundles/gridstack-f9e005145f1f29d3fd436ec6eda8b264c017ee47886472841ed47e32332518ff.css";gon.test_env=false;gon.disable_animations=null;gon.suggested_label_colors={"#cc338b":"Magenta-pink","#dc143c":"Crimson","#c21e56":"Rose red","#cd5b45":"Dark coral","#ed9121":"Carrot orange","#eee600":"Titanium yellow","#009966":"Green-cyan","#8fbc8f":"Dark sea green","#6699cc":"Blue-gray","#e6e6fa":"Lavender","#9400d3":"Dark violet","#330066":"Deep violet","#36454f":"Charcoal grey","#808080":"Gray"};gon.first_day_of_week=0;gon.time_display_relative=true;gon.ee=true;gon.jh=false;gon.dot_com=true;gon.uf_error_prefix="UF";gon.pat_prefix="glpat-";gon.diagramsnet_url="https://embed.diagrams.net";gon.version="16.2.0-pre";gon.current_user_id=9541565;gon.current_username="schneiva";gon.current_user_fullname="Valentin Schneider-Lunitz";gon.current_user_avatar_url="https://secure.gravatar.com/avatar/eefc132cb4b206f0671c7e7aa3e4758d?s=80\u0026d=identicon";gon.use_new_navigation=true;gon.features={"usageDataApi":true,"securityAutoFix":false,"sourceEditorToolbar":false,"vscodeWebIde":true,"unbatchGraphqlQueries":false,"commandPalette":false,"removeMonitorMetrics":true,"gitlabDuo":false,"customEmoji":true,"aiChatHistoryContext":false,"highlightJs":true,"highlightJsWorker":false,"explainCodeChat":false};gon.roadmap_epics_limit=1000;gon.ai={"chat":{"total_model_token":4096,"max_response_token":300,"input_content_limit":15184}};gon.subscriptions_url="https://customers.gitlab.com";gon.subscriptions_legacy_sign_in_url="https://customers.gitlab.com/customers/sign_in?legacy=true";gon.payment_form_url="https://customers.gitlab.com/payment_forms/cc_validation";gon.payment_validation_form_id="payment_method_validation";gon.registration_validation_form_url="https://customers.gitlab.com/payment_forms/cc_registration_validation";
//]]>
</script>


<script src="/assets/webpack/sentry.a2b97a5d.chunk.js" defer="defer" nonce="JrdoIUEtKppIkHqgKvi9kg=="></script>


<script src="/assets/webpack/commons-pages.groups.new-pages.import.gitlab_projects.new-pages.import.manifest.new-pages.projects.n-4e5d09f9.8f20bb20.chunk.js" defer="defer" nonce="JrdoIUEtKppIkHqgKvi9kg=="></script>
<script src="/assets/webpack/commons-pages.search.show-super_sidebar.d8731723.chunk.js" defer="defer" nonce="JrdoIUEtKppIkHqgKvi9kg=="></script>
<script src="/assets/webpack/super_sidebar.89b762e2.chunk.js" defer="defer" nonce="JrdoIUEtKppIkHqgKvi9kg=="></script>
<script src="/assets/webpack/commons-pages.projects-pages.projects.activity-pages.projects.alert_management.details-pages.project-b9313a74.6fbc74ee.chunk.js" defer="defer" nonce="JrdoIUEtKppIkHqgKvi9kg=="></script>
<script src="/assets/webpack/commons-pages.admin.runners.show-pages.groups.achievements-pages.groups.crm.contacts-pages.groups.cr-eadd066d.f37095dd.chunk.js" defer="defer" nonce="JrdoIUEtKppIkHqgKvi9kg=="></script>
<script src="/assets/webpack/commons-pages.projects.blob.show-pages.projects.show-pages.projects.snippets.edit-pages.projects.sni-dd84f7c7.d6969177.chunk.js" defer="defer" nonce="JrdoIUEtKppIkHqgKvi9kg=="></script>
<script src="/assets/webpack/commons-pages.projects.blob.show-pages.projects.show-pages.projects.snippets.show-pages.projects.tre-25c821a4.e3d4ce8a.chunk.js" defer="defer" nonce="JrdoIUEtKppIkHqgKvi9kg=="></script>
<script src="/assets/webpack/commons-pages.groups.show-pages.projects.blob.show-pages.projects.show-pages.projects.tree.show.53d66823.chunk.js" defer="defer" nonce="JrdoIUEtKppIkHqgKvi9kg=="></script>
<script src="/assets/webpack/commons-pages.projects.blob.show-pages.projects.show-pages.projects.tree.show.7e440565.chunk.js" defer="defer" nonce="JrdoIUEtKppIkHqgKvi9kg=="></script>
<script src="/assets/webpack/commons-pages.projects.blob.show-pages.projects.tree.show-treeList.8c6eb22c.chunk.js" defer="defer" nonce="JrdoIUEtKppIkHqgKvi9kg=="></script>
<script src="/assets/webpack/pages.projects.blob.show.ea88dc6a.chunk.js" defer="defer" nonce="JrdoIUEtKppIkHqgKvi9kg=="></script>
<script nonce="JrdoIUEtKppIkHqgKvi9kg==">
//<![CDATA[
window.uploads_path = "/twardzso/espace_eucancan_training_snakemake/uploads";



//]]>
</script>
<meta content="object" property="og:type">
<meta content="GitLab" property="og:site_name">
<meta content="2_cloud/plot-quals.py · master · Sven Twardziok / espace_eucancan_training_snakemake · GitLab" property="og:title">
<meta content="GitLab.com" property="og:description">
<meta content="https://gitlab.com/assets/twitter_card-570ddb06edf56a2312253c5872489847a0f385112ddbcd71ccfa1570febab5d2.jpg" property="og:image">
<meta content="64" property="og:image:width">
<meta content="64" property="og:image:height">
<meta content="https://gitlab.com/twardzso/espace_eucancan_training_snakemake/-/blob/master/2_cloud/plot-quals.py" property="og:url">
<meta content="summary" property="twitter:card">
<meta content="2_cloud/plot-quals.py · master · Sven Twardziok / espace_eucancan_training_snakemake · GitLab" property="twitter:title">
<meta content="GitLab.com" property="twitter:description">
<meta content="https://gitlab.com/assets/twitter_card-570ddb06edf56a2312253c5872489847a0f385112ddbcd71ccfa1570febab5d2.jpg" property="twitter:image">

<meta content="GitLab.com" name="description">
<link href="/-/manifest.json" rel="manifest">
<meta content="width=device-width, initial-scale=1, maximum-scale=1" name="viewport">
<meta content="#292961" name="theme-color">
<meta name="csrf-param" content="authenticity_token" />
<meta name="csrf-token" content="7YpxKGnediHR8Q0FDbeD-P7KXYp7TklWNc0IxRuMJCYZ39UCu-pE7ezo4hVwcZpBF-Wv2Uj5qJERTWz4w6vUvA" />
<meta name="csp-nonce" content="JrdoIUEtKppIkHqgKvi9kg==" />
<meta name="action-cable-url" content="/-/cable" />
<link rel="apple-touch-icon" type="image/x-icon" href="/assets/apple-touch-icon-b049d4bc0dd9626f31db825d61880737befc7835982586d015bded10b4435460.png" />
<link href="/search/opensearch.xml" rel="search" title="Search GitLab" type="application/opensearchdescription+xml">




</head>

<body class="ui-indigo tab-width-8 gl-browser-chrome gl-platform-windows" data-find-file="/twardzso/espace_eucancan_training_snakemake/-/find_file/master" data-namespace-id="5500677" data-page="projects:blob:show" data-page-type-id="master/2_cloud/plot-quals.py" data-project="espace_eucancan_training_snakemake" data-project-id="23446064">

<script nonce="JrdoIUEtKppIkHqgKvi9kg==">
//<![CDATA[
gl = window.gl || {};
gl.client = {"isChrome":true,"isWindows":true};


//]]>
</script>



<style>
  body {
    --header-height: 0px;
  }
</style>
<div class="layout-page hide-when-top-nav-responsive-open page-with-super-sidebar">
<aside class="js-super-sidebar super-sidebar super-sidebar-loading" data-command-palette="{&quot;project_files_url&quot;:&quot;/twardzso/espace_eucancan_training_snakemake/-/files/master?format=json&quot;,&quot;project_blob_url&quot;:&quot;/twardzso/espace_eucancan_training_snakemake/-/blob/master&quot;}" data-force-desktop-expanded-sidebar="" data-root-path="/" data-sidebar="{&quot;current_menu_items&quot;:[{&quot;id&quot;:&quot;project_overview&quot;,&quot;title&quot;:&quot;Project overview&quot;,&quot;icon&quot;:&quot;project&quot;,&quot;link&quot;:&quot;/twardzso/espace_eucancan_training_snakemake&quot;,&quot;pill_count&quot;:null,&quot;link_classes&quot;:&quot;shortcuts-project rspec-project-link&quot;,&quot;is_active&quot;:false},{&quot;title&quot;:&quot;Manage&quot;,&quot;icon&quot;:&quot;users&quot;,&quot;link&quot;:&quot;/twardzso/espace_eucancan_training_snakemake/activity&quot;,&quot;is_active&quot;:false,&quot;pill_count&quot;:null,&quot;items&quot;:[{&quot;id&quot;:&quot;activity&quot;,&quot;title&quot;:&quot;Activity&quot;,&quot;icon&quot;:null,&quot;link&quot;:&quot;/twardzso/espace_eucancan_training_snakemake/activity&quot;,&quot;pill_count&quot;:null,&quot;link_classes&quot;:&quot;shortcuts-project-activity&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;members&quot;,&quot;title&quot;:&quot;Members&quot;,&quot;icon&quot;:null,&quot;link&quot;:&quot;/twardzso/espace_eucancan_training_snakemake/-/project_members&quot;,&quot;pill_count&quot;:null,&quot;link_classes&quot;:null,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;labels&quot;,&quot;title&quot;:&quot;Labels&quot;,&quot;icon&quot;:null,&quot;link&quot;:&quot;/twardzso/espace_eucancan_training_snakemake/-/labels&quot;,&quot;pill_count&quot;:null,&quot;link_classes&quot;:null,&quot;is_active&quot;:false}],&quot;separated&quot;:false},{&quot;title&quot;:&quot;Plan&quot;,&quot;icon&quot;:&quot;planning&quot;,&quot;link&quot;:&quot;/twardzso/espace_eucancan_training_snakemake/-/issues&quot;,&quot;is_active&quot;:false,&quot;pill_count&quot;:null,&quot;items&quot;:[{&quot;id&quot;:&quot;project_issue_list&quot;,&quot;title&quot;:&quot;Issues&quot;,&quot;icon&quot;:null,&quot;link&quot;:&quot;/twardzso/espace_eucancan_training_snakemake/-/issues&quot;,&quot;pill_count&quot;:&quot;0&quot;,&quot;link_classes&quot;:&quot;shortcuts-issues has-sub-items&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;boards&quot;,&quot;title&quot;:&quot;Issue boards&quot;,&quot;icon&quot;:null,&quot;link&quot;:&quot;/twardzso/espace_eucancan_training_snakemake/-/boards&quot;,&quot;pill_count&quot;:null,&quot;link_classes&quot;:&quot;shortcuts-issue-boards&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;milestones&quot;,&quot;title&quot;:&quot;Milestones&quot;,&quot;icon&quot;:null,&quot;link&quot;:&quot;/twardzso/espace_eucancan_training_snakemake/-/milestones&quot;,&quot;pill_count&quot;:null,&quot;link_classes&quot;:null,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;project_wiki&quot;,&quot;title&quot;:&quot;Wiki&quot;,&quot;icon&quot;:null,&quot;link&quot;:&quot;/twardzso/espace_eucancan_training_snakemake/-/wikis/home&quot;,&quot;pill_count&quot;:null,&quot;link_classes&quot;:&quot;shortcuts-wiki&quot;,&quot;is_active&quot;:false}],&quot;separated&quot;:false},{&quot;title&quot;:&quot;Code&quot;,&quot;icon&quot;:&quot;code&quot;,&quot;link&quot;:&quot;/twardzso/espace_eucancan_training_snakemake/-/merge_requests&quot;,&quot;is_active&quot;:true,&quot;pill_count&quot;:null,&quot;items&quot;:[{&quot;id&quot;:&quot;project_merge_request_list&quot;,&quot;title&quot;:&quot;Merge requests&quot;,&quot;icon&quot;:null,&quot;link&quot;:&quot;/twardzso/espace_eucancan_training_snakemake/-/merge_requests&quot;,&quot;pill_count&quot;:&quot;0&quot;,&quot;link_classes&quot;:&quot;shortcuts-merge_requests&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;files&quot;,&quot;title&quot;:&quot;Repository&quot;,&quot;icon&quot;:null,&quot;link&quot;:&quot;/twardzso/espace_eucancan_training_snakemake/-/tree/master&quot;,&quot;pill_count&quot;:null,&quot;link_classes&quot;:&quot;shortcuts-tree&quot;,&quot;is_active&quot;:true},{&quot;id&quot;:&quot;branches&quot;,&quot;title&quot;:&quot;Branches&quot;,&quot;icon&quot;:null,&quot;link&quot;:&quot;/twardzso/espace_eucancan_training_snakemake/-/branches&quot;,&quot;pill_count&quot;:null,&quot;link_classes&quot;:null,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;commits&quot;,&quot;title&quot;:&quot;Commits&quot;,&quot;icon&quot;:null,&quot;link&quot;:&quot;/twardzso/espace_eucancan_training_snakemake/-/commits/master?ref_type=heads&quot;,&quot;pill_count&quot;:null,&quot;link_classes&quot;:&quot;shortcuts-commits&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;tags&quot;,&quot;title&quot;:&quot;Tags&quot;,&quot;icon&quot;:null,&quot;link&quot;:&quot;/twardzso/espace_eucancan_training_snakemake/-/tags&quot;,&quot;pill_count&quot;:null,&quot;link_classes&quot;:null,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;graphs&quot;,&quot;title&quot;:&quot;Repository graph&quot;,&quot;icon&quot;:null,&quot;link&quot;:&quot;/twardzso/espace_eucancan_training_snakemake/-/network/master?ref_type=heads&quot;,&quot;pill_count&quot;:null,&quot;link_classes&quot;:&quot;shortcuts-network&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;compare&quot;,&quot;title&quot;:&quot;Compare revisions&quot;,&quot;icon&quot;:null,&quot;link&quot;:&quot;/twardzso/espace_eucancan_training_snakemake/-/compare?from=master\u0026to=master&quot;,&quot;pill_count&quot;:null,&quot;link_classes&quot;:null,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;project_snippets&quot;,&quot;title&quot;:&quot;Snippets&quot;,&quot;icon&quot;:null,&quot;link&quot;:&quot;/twardzso/espace_eucancan_training_snakemake/-/snippets&quot;,&quot;pill_count&quot;:null,&quot;link_classes&quot;:&quot;shortcuts-snippets&quot;,&quot;is_active&quot;:false}],&quot;separated&quot;:false},{&quot;title&quot;:&quot;Build&quot;,&quot;icon&quot;:&quot;rocket&quot;,&quot;link&quot;:&quot;/twardzso/espace_eucancan_training_snakemake/-/pipelines&quot;,&quot;is_active&quot;:false,&quot;pill_count&quot;:null,&quot;items&quot;:[{&quot;id&quot;:&quot;pipelines&quot;,&quot;title&quot;:&quot;Pipelines&quot;,&quot;icon&quot;:null,&quot;link&quot;:&quot;/twardzso/espace_eucancan_training_snakemake/-/pipelines&quot;,&quot;pill_count&quot;:null,&quot;link_classes&quot;:&quot;shortcuts-pipelines&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;jobs&quot;,&quot;title&quot;:&quot;Jobs&quot;,&quot;icon&quot;:null,&quot;link&quot;:&quot;/twardzso/espace_eucancan_training_snakemake/-/jobs&quot;,&quot;pill_count&quot;:null,&quot;link_classes&quot;:&quot;shortcuts-builds&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;pipeline_schedules&quot;,&quot;title&quot;:&quot;Pipeline schedules&quot;,&quot;icon&quot;:null,&quot;link&quot;:&quot;/twardzso/espace_eucancan_training_snakemake/-/pipeline_schedules&quot;,&quot;pill_count&quot;:null,&quot;link_classes&quot;:&quot;shortcuts-builds&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;artifacts&quot;,&quot;title&quot;:&quot;Artifacts&quot;,&quot;icon&quot;:null,&quot;link&quot;:&quot;/twardzso/espace_eucancan_training_snakemake/-/artifacts&quot;,&quot;pill_count&quot;:null,&quot;link_classes&quot;:&quot;shortcuts-builds&quot;,&quot;is_active&quot;:false}],&quot;separated&quot;:false},{&quot;title&quot;:&quot;Deploy&quot;,&quot;icon&quot;:&quot;deployments&quot;,&quot;link&quot;:&quot;/twardzso/espace_eucancan_training_snakemake/-/releases&quot;,&quot;is_active&quot;:false,&quot;pill_count&quot;:null,&quot;items&quot;:[{&quot;id&quot;:&quot;releases&quot;,&quot;title&quot;:&quot;Releases&quot;,&quot;icon&quot;:null,&quot;link&quot;:&quot;/twardzso/espace_eucancan_training_snakemake/-/releases&quot;,&quot;pill_count&quot;:null,&quot;link_classes&quot;:&quot;shortcuts-deployments-releases&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;packages_registry&quot;,&quot;title&quot;:&quot;Package Registry&quot;,&quot;icon&quot;:null,&quot;link&quot;:&quot;/twardzso/espace_eucancan_training_snakemake/-/packages&quot;,&quot;pill_count&quot;:null,&quot;link_classes&quot;:&quot;shortcuts-container-registry&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;container_registry&quot;,&quot;title&quot;:&quot;Container Registry&quot;,&quot;icon&quot;:null,&quot;link&quot;:&quot;/twardzso/espace_eucancan_training_snakemake/container_registry&quot;,&quot;pill_count&quot;:null,&quot;link_classes&quot;:null,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;model_experiments&quot;,&quot;title&quot;:&quot;Model experiments&quot;,&quot;icon&quot;:null,&quot;link&quot;:&quot;/twardzso/espace_eucancan_training_snakemake/-/ml/experiments&quot;,&quot;pill_count&quot;:null,&quot;link_classes&quot;:null,&quot;is_active&quot;:false}],&quot;separated&quot;:false},{&quot;title&quot;:&quot;Operate&quot;,&quot;icon&quot;:&quot;cloud-pod&quot;,&quot;link&quot;:&quot;/twardzso/espace_eucancan_training_snakemake/-/environments&quot;,&quot;is_active&quot;:false,&quot;pill_count&quot;:null,&quot;items&quot;:[{&quot;id&quot;:&quot;environments&quot;,&quot;title&quot;:&quot;Environments&quot;,&quot;icon&quot;:null,&quot;link&quot;:&quot;/twardzso/espace_eucancan_training_snakemake/-/environments&quot;,&quot;pill_count&quot;:null,&quot;link_classes&quot;:&quot;shortcuts-environments&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;infrastructure_registry&quot;,&quot;title&quot;:&quot;Terraform modules&quot;,&quot;icon&quot;:null,&quot;link&quot;:&quot;/twardzso/espace_eucancan_training_snakemake/-/infrastructure_registry&quot;,&quot;pill_count&quot;:null,&quot;link_classes&quot;:null,&quot;is_active&quot;:false}],&quot;separated&quot;:false},{&quot;title&quot;:&quot;Monitor&quot;,&quot;icon&quot;:&quot;monitor&quot;,&quot;link&quot;:&quot;/twardzso/espace_eucancan_training_snakemake/-/incidents&quot;,&quot;is_active&quot;:false,&quot;pill_count&quot;:null,&quot;items&quot;:[{&quot;id&quot;:&quot;incidents&quot;,&quot;title&quot;:&quot;Incidents&quot;,&quot;icon&quot;:null,&quot;link&quot;:&quot;/twardzso/espace_eucancan_training_snakemake/-/incidents&quot;,&quot;pill_count&quot;:null,&quot;link_classes&quot;:null,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;service_desk&quot;,&quot;title&quot;:&quot;Service Desk&quot;,&quot;icon&quot;:null,&quot;link&quot;:&quot;/twardzso/espace_eucancan_training_snakemake/-/issues/service_desk&quot;,&quot;pill_count&quot;:null,&quot;link_classes&quot;:null,&quot;is_active&quot;:false}],&quot;separated&quot;:false},{&quot;title&quot;:&quot;Analyze&quot;,&quot;icon&quot;:&quot;chart&quot;,&quot;link&quot;:&quot;/twardzso/espace_eucancan_training_snakemake/-/value_stream_analytics&quot;,&quot;is_active&quot;:false,&quot;pill_count&quot;:null,&quot;items&quot;:[{&quot;id&quot;:&quot;cycle_analytics&quot;,&quot;title&quot;:&quot;Value stream analytics&quot;,&quot;icon&quot;:null,&quot;link&quot;:&quot;/twardzso/espace_eucancan_training_snakemake/-/value_stream_analytics&quot;,&quot;pill_count&quot;:null,&quot;link_classes&quot;:&quot;shortcuts-project-cycle-analytics&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;contributors&quot;,&quot;title&quot;:&quot;Contributor statistics&quot;,&quot;icon&quot;:null,&quot;link&quot;:&quot;/twardzso/espace_eucancan_training_snakemake/-/graphs/master?ref_type=heads&quot;,&quot;pill_count&quot;:null,&quot;link_classes&quot;:null,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;ci_cd_analytics&quot;,&quot;title&quot;:&quot;CI/CD analytics&quot;,&quot;icon&quot;:null,&quot;link&quot;:&quot;/twardzso/espace_eucancan_training_snakemake/-/pipelines/charts&quot;,&quot;pill_count&quot;:null,&quot;link_classes&quot;:null,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;repository_analytics&quot;,&quot;title&quot;:&quot;Repository analytics&quot;,&quot;icon&quot;:null,&quot;link&quot;:&quot;/twardzso/espace_eucancan_training_snakemake/-/graphs/master/charts&quot;,&quot;pill_count&quot;:null,&quot;link_classes&quot;:&quot;shortcuts-repository-charts&quot;,&quot;is_active&quot;:false}],&quot;separated&quot;:false}],&quot;current_context_header&quot;:{&quot;title&quot;:&quot;espace_eucancan_training_snakemake&quot;,&quot;avatar&quot;:null,&quot;id&quot;:23446064},&quot;name&quot;:&quot;Valentin Schneider-Lunitz&quot;,&quot;username&quot;:&quot;schneiva&quot;,&quot;avatar_url&quot;:&quot;https://secure.gravatar.com/avatar/eefc132cb4b206f0671c7e7aa3e4758d?s=80\u0026d=identicon&quot;,&quot;has_link_to_profile&quot;:true,&quot;link_to_profile&quot;:&quot;https://gitlab.com/schneiva&quot;,&quot;logo_url&quot;:null,&quot;status&quot;:{&quot;can_update&quot;:true,&quot;busy&quot;:null,&quot;customized&quot;:null,&quot;availability&quot;:&quot;&quot;,&quot;emoji&quot;:null,&quot;message_html&quot;:null,&quot;message&quot;:null,&quot;clear_after&quot;:null},&quot;settings&quot;:{&quot;has_settings&quot;:true,&quot;profile_path&quot;:&quot;/-/profile&quot;,&quot;profile_preferences_path&quot;:&quot;/-/profile/preferences&quot;},&quot;user_counts&quot;:{&quot;assigned_issues&quot;:6,&quot;assigned_merge_requests&quot;:0,&quot;review_requested_merge_requests&quot;:0,&quot;todos&quot;:10,&quot;last_update&quot;:1688991497035},&quot;can_sign_out&quot;:true,&quot;sign_out_link&quot;:&quot;/users/sign_out&quot;,&quot;issues_dashboard_path&quot;:&quot;/dashboard/issues?assignee_username=schneiva&quot;,&quot;todos_dashboard_path&quot;:&quot;/dashboard/todos&quot;,&quot;create_new_menu_groups&quot;:[{&quot;name&quot;:&quot;In this project&quot;,&quot;items&quot;:[{&quot;text&quot;:&quot;New issue&quot;,&quot;href&quot;:&quot;/twardzso/espace_eucancan_training_snakemake/-/issues/new&quot;,&quot;component&quot;:null,&quot;extraAttrs&quot;:{&quot;data-track-label&quot;:&quot;new_issue&quot;,&quot;data-track-action&quot;:&quot;click_link&quot;,&quot;data-track-property&quot;:&quot;nav_create_menu&quot;,&quot;data-testid&quot;:&quot;create_menu_item&quot;,&quot;data-qa-create-menu-item&quot;:&quot;new_issue&quot;}}]},{&quot;name&quot;:&quot;In GitLab&quot;,&quot;items&quot;:[{&quot;text&quot;:&quot;New project/repository&quot;,&quot;href&quot;:&quot;/projects/new&quot;,&quot;component&quot;:null,&quot;extraAttrs&quot;:{&quot;data-track-label&quot;:&quot;general_new_project&quot;,&quot;data-track-action&quot;:&quot;click_link&quot;,&quot;data-track-property&quot;:&quot;nav_create_menu&quot;,&quot;data-testid&quot;:&quot;create_menu_item&quot;,&quot;data-qa-create-menu-item&quot;:&quot;general_new_project&quot;}},{&quot;text&quot;:&quot;New group&quot;,&quot;href&quot;:&quot;/groups/new&quot;,&quot;component&quot;:null,&quot;extraAttrs&quot;:{&quot;data-track-label&quot;:&quot;general_new_group&quot;,&quot;data-track-action&quot;:&quot;click_link&quot;,&quot;data-track-property&quot;:&quot;nav_create_menu&quot;,&quot;data-testid&quot;:&quot;create_menu_item&quot;,&quot;data-qa-create-menu-item&quot;:&quot;general_new_group&quot;}},{&quot;text&quot;:&quot;New snippet&quot;,&quot;href&quot;:&quot;/-/snippets/new&quot;,&quot;component&quot;:null,&quot;extraAttrs&quot;:{&quot;data-track-label&quot;:&quot;general_new_snippet&quot;,&quot;data-track-action&quot;:&quot;click_link&quot;,&quot;data-track-property&quot;:&quot;nav_create_menu&quot;,&quot;data-testid&quot;:&quot;create_menu_item&quot;,&quot;data-qa-create-menu-item&quot;:&quot;general_new_snippet&quot;}}]}],&quot;merge_request_menu&quot;:[{&quot;name&quot;:&quot;Merge requests&quot;,&quot;items&quot;:[{&quot;text&quot;:&quot;Assigned&quot;,&quot;href&quot;:&quot;/dashboard/merge_requests?assignee_username=schneiva&quot;,&quot;count&quot;:0,&quot;userCount&quot;:&quot;assigned_merge_requests&quot;,&quot;extraAttrs&quot;:{&quot;data-track-action&quot;:&quot;click_link&quot;,&quot;data-track-label&quot;:&quot;merge_requests_assigned&quot;,&quot;data-track-property&quot;:&quot;nav_core_menu&quot;,&quot;class&quot;:&quot;dashboard-shortcuts-merge_requests&quot;}},{&quot;text&quot;:&quot;Review requests&quot;,&quot;href&quot;:&quot;/dashboard/merge_requests?reviewer_username=schneiva&quot;,&quot;count&quot;:0,&quot;userCount&quot;:&quot;review_requested_merge_requests&quot;,&quot;extraAttrs&quot;:{&quot;data-track-action&quot;:&quot;click_link&quot;,&quot;data-track-label&quot;:&quot;merge_requests_to_review&quot;,&quot;data-track-property&quot;:&quot;nav_core_menu&quot;,&quot;class&quot;:&quot;dashboard-shortcuts-review_requests&quot;}}]}],&quot;projects_path&quot;:&quot;/dashboard/projects&quot;,&quot;groups_path&quot;:&quot;/dashboard/groups&quot;,&quot;support_path&quot;:&quot;https://about.gitlab.com/get-help/&quot;,&quot;display_whats_new&quot;:true,&quot;whats_new_most_recent_release_items_count&quot;:5,&quot;whats_new_version_digest&quot;:&quot;981955e703369178cb87cbb7a2075060174b67907a3a4967a5a07e9d9281739e&quot;,&quot;show_version_check&quot;:false,&quot;gitlab_version&quot;:{&quot;major&quot;:16,&quot;minor&quot;:2,&quot;patch&quot;:0,&quot;suffix_s&quot;:&quot;&quot;},&quot;gitlab_version_check&quot;:{&quot;latest_stable_versions&quot;:[],&quot;latest_version&quot;:&quot;16.1.2&quot;,&quot;severity&quot;:&quot;success&quot;,&quot;critical_vulnerability&quot;:false,&quot;details&quot;:&quot;&quot;},&quot;gitlab_com_but_not_canary&quot;:true,&quot;gitlab_com_and_canary&quot;:null,&quot;canary_toggle_com_url&quot;:&quot;https://next.gitlab.com&quot;,&quot;current_context&quot;:{&quot;namespace&quot;:&quot;projects&quot;,&quot;item&quot;:{&quot;id&quot;:23446064,&quot;name&quot;:&quot;espace_eucancan_training_snakemake&quot;,&quot;namespace&quot;:&quot;Sven Twardziok / espace_eucancan_training_snakemake&quot;,&quot;webUrl&quot;:&quot;/twardzso/espace_eucancan_training_snakemake&quot;,&quot;avatarUrl&quot;:null}},&quot;context_switcher_links&quot;:[{&quot;title&quot;:&quot;Your work&quot;,&quot;link&quot;:&quot;/&quot;,&quot;icon&quot;:&quot;work&quot;},{&quot;title&quot;:&quot;Explore&quot;,&quot;link&quot;:&quot;/explore&quot;,&quot;icon&quot;:&quot;compass&quot;}],&quot;search&quot;:{&quot;search_path&quot;:&quot;/search&quot;,&quot;issues_path&quot;:&quot;/dashboard/issues&quot;,&quot;mr_path&quot;:&quot;/dashboard/merge_requests&quot;,&quot;autocomplete_path&quot;:&quot;/search/autocomplete&quot;,&quot;search_context&quot;:{&quot;project&quot;:{&quot;id&quot;:23446064,&quot;name&quot;:&quot;espace_eucancan_training_snakemake&quot;},&quot;project_metadata&quot;:{&quot;mr_path&quot;:&quot;/twardzso/espace_eucancan_training_snakemake/-/merge_requests&quot;,&quot;issues_path&quot;:&quot;/twardzso/espace_eucancan_training_snakemake/-/issues&quot;},&quot;code_search&quot;:true,&quot;ref&quot;:&quot;master&quot;,&quot;scope&quot;:null,&quot;for_snippets&quot;:null}},&quot;pinned_items&quot;:[&quot;project_issue_list&quot;,&quot;project_merge_request_list&quot;],&quot;panel_type&quot;:&quot;project&quot;,&quot;update_pins_url&quot;:&quot;https://gitlab.com/-/users/pins&quot;,&quot;is_impersonating&quot;:false,&quot;stop_impersonation_path&quot;:&quot;/admin/impersonation&quot;,&quot;shortcut_links&quot;:[{&quot;title&quot;:&quot;Milestones&quot;,&quot;href&quot;:&quot;/dashboard/milestones&quot;,&quot;css_class&quot;:&quot;dashboard-shortcuts-milestones&quot;},{&quot;title&quot;:&quot;Snippets&quot;,&quot;href&quot;:&quot;/dashboard/snippets&quot;,&quot;css_class&quot;:&quot;dashboard-shortcuts-snippets&quot;},{&quot;title&quot;:&quot;Activity&quot;,&quot;href&quot;:&quot;/dashboard/activity&quot;,&quot;css_class&quot;:&quot;dashboard-shortcuts-activity&quot;},{&quot;title&quot;:&quot;Create a new issue&quot;,&quot;href&quot;:&quot;/twardzso/espace_eucancan_training_snakemake/-/issues/new&quot;,&quot;css_class&quot;:&quot;shortcuts-new-issue&quot;}],&quot;show_tanuki_bot&quot;:false,&quot;trial&quot;:{&quot;has_start_trial&quot;:false,&quot;url&quot;:&quot;/-/trials/new?glm_content=top-right-dropdown\u0026glm_source=gitlab.com&quot;}}" data-toggle-new-nav-endpoint="https://gitlab.com/-/profile/preferences"></aside>
<div data-version-digest="981955e703369178cb87cbb7a2075060174b67907a3a4967a5a07e9d9281739e" id="whats-new-app"></div>

<div class="content-wrapper">
<div class="mobile-overlay"></div>

<div class="alert-wrapper gl-force-block-formatting-context">



























<div class="top-bar-fixed container-fluid">
<div class="top-bar-container gl-display-flex gl-align-items-center">
<button class="gl-button btn btn-icon btn-md btn-default btn-default-tertiary js-super-sidebar-toggle-expand super-sidebar-toggle gl-ml-n3 gl-mr-2" title="Expand sidebar" aria-controls="super-sidebar" aria-expanded="false" aria-label="Navigation sidebar" type="button"><svg class="s16 gl-icon gl-button-icon " data-testid="sidebar-icon"><use href="/assets/icons-b8c5a9711f73b1de3c81754da0aca72f43b0e6844aa06dd03092b601a493f45b.svg#sidebar"></use></svg>

</button>
<nav aria-label="Breadcrumbs" class="breadcrumbs" data-qa-selector="breadcrumb_links_content" data-testid="breadcrumb-links">
<ul class="list-unstyled breadcrumbs-list js-breadcrumbs-list">
<li><a href="/twardzso">Sven Twardziok</a><svg class="s8 breadcrumbs-list-angle" data-testid="chevron-lg-right-icon"><use href="/assets/icons-b8c5a9711f73b1de3c81754da0aca72f43b0e6844aa06dd03092b601a493f45b.svg#chevron-lg-right"></use></svg></li> <li><a href="/twardzso/espace_eucancan_training_snakemake"><span class="breadcrumb-item-text js-breadcrumb-item-text">espace_eucancan_training_snakemake</span></a><svg class="s8 breadcrumbs-list-angle" data-testid="chevron-lg-right-icon"><use href="/assets/icons-b8c5a9711f73b1de3c81754da0aca72f43b0e6844aa06dd03092b601a493f45b.svg#chevron-lg-right"></use></svg></li>

<li data-qa-selector="breadcrumb_current_link" data-testid="breadcrumb-current-link">
<a href="/twardzso/espace_eucancan_training_snakemake/-/blob/master/2_cloud/plot-quals.py">Repository</a>
</li>
</ul>
<script type="application/ld+json">
{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Sven Twardziok","item":"https://gitlab.com/twardzso"},{"@type":"ListItem","position":2,"name":"espace_eucancan_training_snakemake","item":"https://gitlab.com/twardzso/espace_eucancan_training_snakemake"},{"@type":"ListItem","position":3,"name":"Repository","item":"https://gitlab.com/twardzso/espace_eucancan_training_snakemake/-/blob/master/2_cloud/plot-quals.py"}]}

</script>
</nav>


</div>
</div>

</div>
<div class="container-fluid container-limited project-highlight-puc">
<main class="content" id="content-body" itemscope itemtype="http://schema.org/SoftwareSourceCode">
<div class="flash-container flash-container-page sticky" data-qa-selector="flash_container">
</div>




<div class="js-signature-container" data-signatures-path="/twardzso/espace_eucancan_training_snakemake/-/commits/8005a5bbf9c63b70b2b433eb7a9fc9671396e1ee/signatures?limit=1"></div>

<div class="tree-holder" id="tree-holder">
<div class="nav-block">
<div class="tree-ref-container">
<div class="tree-ref-holder">
<div data-project-id="23446064" data-project-root-path="/twardzso/espace_eucancan_training_snakemake" data-ref="master" data-ref-type="" id="js-tree-ref-switcher"></div>
</div>
<ul class="breadcrumb repo-breadcrumb">
<li class="breadcrumb-item">
<a href="/twardzso/espace_eucancan_training_snakemake/-/tree/master">espace_eucancan_training_snakemake
</a></li>
<li class="breadcrumb-item">
<a href="/twardzso/espace_eucancan_training_snakemake/-/tree/master/2_cloud">2_cloud</a>
</li>
<li class="breadcrumb-item">
<a href="/twardzso/espace_eucancan_training_snakemake/-/blob/master/2_cloud/plot-quals.py"><strong>plot-quals.py</strong>
</a></li>
</ul>
</div>
<div class="tree-controls gl-children-ml-sm-3"><a class="gl-button btn btn-md btn-default shortcuts-find-file" rel="nofollow" href="/twardzso/espace_eucancan_training_snakemake/-/find_file/master"><span class="gl-button-text">
Find file

</span>

</a><a class="gl-button btn btn-default js-blob-blame-link" href="/twardzso/espace_eucancan_training_snakemake/-/blame/master/2_cloud/plot-quals.py">Blame</a><a class="gl-button btn btn-default" href="/twardzso/espace_eucancan_training_snakemake/-/commits/master/2_cloud/plot-quals.py">History</a><a class="gl-button btn btn-default js-data-file-blob-permalink-url" href="/twardzso/espace_eucancan_training_snakemake/-/blob/607cde6aabdc80e9623ac562007cb3b4720b0910/2_cloud/plot-quals.py">Permalink</a></div>
</div>

<div class="info-well d-none d-sm-block">
<div class="well-segment">
<ul class="blob-commit-info">
<li class="commit flex-row js-toggle-container" id="commit-8005a5bb">
<div class="avatar-cell d-none d-sm-block">
<a href="/twardzso"><img alt="Sven Twardziok&#39;s avatar" src="https://secure.gravatar.com/avatar/1257a2f65cd4efc94bfe0e94aeac0823?s=80&amp;d=identicon" class="avatar s40 d-none d-sm-inline-block" title="Sven Twardziok"></a>
</div>
<div class="commit-detail flex-list gl-display-flex gl-justify-content-space-between gl-align-items-flex-start gl-flex-grow-1 gl-min-w-0">
<div class="commit-content" data-qa-selector="commit_content">
<a class="commit-row-message item-title js-onboarding-commit-item " href="/twardzso/espace_eucancan_training_snakemake/-/commit/8005a5bbf9c63b70b2b433eb7a9fc9671396e1ee">update structure</a>
<span class="commit-row-message d-inline d-sm-none">
&middot;
8005a5bb
</span>
<div class="committer">
<a class="commit-author-link js-user-link" data-user-id="4197334" href="/twardzso">Sven Twardziok</a> authored <time class="js-timeago" title="Jan 12, 2021 7:57am" datetime="2021-01-12T07:57:35Z" data-toggle="tooltip" data-placement="bottom" data-container="body">Jan 12, 2021</time>
</div>

</div>
<div class="commit-actions flex-row">

<div class="js-commit-pipeline-status" data-endpoint="/twardzso/espace_eucancan_training_snakemake/-/commit/8005a5bbf9c63b70b2b433eb7a9fc9671396e1ee/pipelines?ref=master"></div>
<div class="commit-sha-group btn-group d-none d-sm-flex">
<div class="label label-monospace monospace">
8005a5bb
</div>
<button class="btn gl-button btn btn-default btn-icon" data-toggle="tooltip" data-placement="bottom" data-container="body" data-clipboard-text="8005a5bbf9c63b70b2b433eb7a9fc9671396e1ee" type="button" title="Copy commit SHA" aria-label="Copy commit SHA" aria-live="polite"><svg class="s16 gl-icon" data-testid="copy-to-clipboard-icon"><use href="/assets/icons-b8c5a9711f73b1de3c81754da0aca72f43b0e6844aa06dd03092b601a493f45b.svg#copy-to-clipboard"></use></svg></button>

</div>
</div>
</div>
</li>

</ul>
</div>

</div>
<div class="blob-content-holder js-per-page" data-blame-per-page="1000" id="blob-content-holder">
<div data-blob-path="2_cloud/plot-quals.py" data-explain-code-available="false" data-original-branch="master" data-project-path="twardzso/espace_eucancan_training_snakemake" data-resource-id="gid://gitlab/Project/23446064" data-target-branch="master" data-user-id="gid://gitlab/User/9541565" id="js-view-blob-app">
<div class="gl-spinner-container" role="status"><span aria-label="Loading" class="gl-spinner gl-spinner-md gl-spinner-dark gl-vertical-align-text-bottom!"></span></div>
</div>
</div>

</div>

<script nonce="JrdoIUEtKppIkHqgKvi9kg==">
//<![CDATA[
  window.gl = window.gl || {};
  window.gl.webIDEPath = '/-/ide/project/schneiva/espace_eucancan_training_snakemake/edit/master/-/2_cloud/plot-quals.py'


//]]>
</script>

</main>
</div>


</div>
</div>



<script nonce="JrdoIUEtKppIkHqgKvi9kg==">
//<![CDATA[
if ('loading' in HTMLImageElement.prototype) {
  document.querySelectorAll('img.lazy').forEach(img => {
    img.loading = 'lazy';
    let imgUrl = img.dataset.src;
    // Only adding width + height for avatars for now
    if (imgUrl.indexOf('/avatar/') > -1 && imgUrl.indexOf('?') === -1) {
      const targetWidth = img.getAttribute('width') || img.width;
      imgUrl += `?width=${targetWidth}`;
    }
    img.src = imgUrl;
    img.removeAttribute('data-src');
    img.classList.remove('lazy');
    img.classList.add('js-lazy-loaded');
    img.dataset.qa_selector = 'js_lazy_loaded_content';
  });
}

//]]>
</script>
<script nonce="JrdoIUEtKppIkHqgKvi9kg==">
//<![CDATA[
gl = window.gl || {};
gl.experiments = {};


//]]>
</script>

</body>
</html>

