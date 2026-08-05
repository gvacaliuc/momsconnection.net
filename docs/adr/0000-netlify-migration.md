# ADR 0000: Migrate Hosting and Form Handling to Netlify

- Status: Proposed
- Date: 2026-08-04
- Decision owners: Site maintainers

## Context

Mom's Connection is a static Hugo site currently built and deployed to GitHub
Pages by GitHub Actions. The Services page includes a contact form, but GitHub
Pages cannot process submissions. We need a reliable way for prospective
clients to contact Mom's Connection without paying for a separate form service
or maintaining an application backend.

The site should remain inexpensive and simple to operate. Form submissions
must be reviewable outside an email inbox, notify the site owner by email, and
include basic spam protection. The hosting platform must continue to support
the custom `momsconnection.net` domain and automated deployments from GitHub.

## Decision

Migrate production hosting from GitHub Pages to Netlify and use Netlify Forms
for contact-form processing.

The GitHub repository will remain the source of truth. Netlify will build the
site with Hugo `0.153.1`, publish the generated `public/` directory, and deploy
production from the repository's default branch. Deploy previews may be used
for pull requests.

The contact form will:

- use Netlify's static HTML form detection;
- submit the visitor's name, phone number, email address, due date, and message;
- mark the appropriate fields as required and use native browser validation;
- include a honeypot field for basic spam protection;
- redirect successful submissions to a custom thank-you page;
- store submissions in the Netlify dashboard; and
- send submission notifications to `karen@momsconnection.net`.

No custom server, serverless function, or third-party form processor will be
introduced unless Netlify Forms proves insufficient.

## Rationale

Netlify provides static hosting, Git-based deployments, custom-domain TLS, and
form processing in one service. This preserves Hugo's simple static
architecture while avoiding the cost and operational work of a separate form
provider or custom backend.

At the time of this decision, Netlify offers a free hosting tier and free form
submissions. Usage limits and pricing should be confirmed when the site is
connected because provider terms may change.

## Alternatives Considered

### Continue using GitHub Pages with a hosted form service

Services such as Formspree would require another account and may introduce a
separate recurring charge. This also splits hosting and form operations across
two providers.

### Deploy a custom application to Fly.io

A custom endpoint would provide full control, but it would also require email
delivery, secrets management, spam prevention, logging, monitoring, and ongoing
application maintenance. That complexity is not justified for the current
contact form.

### Use a `mailto:` form or link

This depends on the visitor having a correctly configured email application,
provides a poor mobile experience, and offers no reliable delivery or
submission history.
