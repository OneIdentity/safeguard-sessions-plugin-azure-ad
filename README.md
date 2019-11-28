# safeguard-sessions-plugin-azure-ad
Microsoft Azure Active Directory plugin for Safeguard for Privileged Sessions

# Support
- This plugin is experimental.

- We welcome feature requests, pull requests, and bug reports submitted via GitHub.com, but in this case there is no guaranteed response time.

# About us

One Identity solutions eliminate the complexities and time-consuming processes often required to govern identities, manage privileged accounts and control access. Our solutions enhance business agility while addressing your IAM challenges with on-premises, cloud and hybrid environments.

# Contacting us

For sales or other inquiries, visit the [One Identity Contact page](https://www.oneidentity.com/company/contact-us.aspx) or call +1-800-306-9329.

# Technical support resources

Technical support is available to One Identity customers with a valid maintenance contract and customers who have trial versions. You can access the Support Portal at the [One Identity Support page](https://support.oneidentity.com/).

The Support Portal provides self-help tools you can use to solve problems quickly and independently, 24 hours a day, 365 days a year. The Support Portal enables you to:

- Submit and manage a Service Request
- View Knowledge Base articles
- Sign up for product notifications
- Download software and technical documentation
- View how-to-videos at [YouTube](https://www.YouTube.com/OneIdentity)
- Engage in community discussions
- Chat with support engineers online
- View services to assist you with your product

# OAuth 2.0

Relation to OAuth 2.0 RFC7649, RFC8252.

## Terminology

OAuth 2.0 defines several concepts and roles. This section provides a mapping between OAuth 2.0 and SPS terminology.

The OAuth 2.0 resource owner is identified as the gateway user in an SPS session. The gateway user may be a human, thus we sometimes refer to it as end-user.

User-agent is the gateway user's web browser.

Resource server is an SPS (virtual) appliance.

Client is again the SPS appliance as Safeguard does not require additional agent installation at the end-user.

Authorization server is a Microsoft Azure AD, also known as Login server.

## Grant flow

Azure AD for SPS plugin utilizes the [Device code flow](https://github.com/AzureAD/microsoft-authentication-library-for-dotnet/wiki/Device-Code-Flow). For further design details see [OAuth 2.0 device authorization grant flow](https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-device-code).

## Pre-requisites

Add a new application to your Azure AD on the Azure Portal, see [Quickstart: Register an application with the Microsoft identity platform](https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app).

Leave "Redirect URIs" empty as it is not required for the device code flow.

Make sure to set "Treat client application as a public client" to YES in the "Authentication" settings.
