Changelog
=========

0.5.25 (unreleased)
-------------------

- Nothing changed yet.


0.5.24 (2017-09-08)
-------------------

- Nothing changed yet.


0.5.23 (2017-09-05)
-------------------

- Nothing changed yet.


0.5.22 (2017-09-01)
-------------------

- Clear right-actions-viewlet.
  [osnickers].


0.5.21 (2017-08-31)
-------------------

- Fix print margin problem when there is a portlet : #18514
  [laulaz]


0.5.20 (2017-08-31)
-------------------

- Fix bad release
  [boulch]


0.5.19 (2017-08-31)
-------------------

- Update styles.less
  [osnickers]


0.5.18 (2017-08-29)
-------------------

- Fix blank page print problem : #18514
  [laulaz]


0.5.17 (2017-08-25)
-------------------

- Add is_folder_view theme parameter : #18467
  [laulaz]

- Avoid camelcase in manifest.cfg
  See http://blog.affinitic.be/2014/08/12/beware-of-uppercase-letters-in-your-config-files/
  [laulaz]

- Remove useless social links on contact card
  [laulaz]

- Use new div to be able to fill schedule, etc. in Diazo even if activity is
  empty : #18469
  [laulaz]


0.5.16 (2017-08-24)
-------------------

- Change css for image to contact.
  [mgennart]


0.5.15 (2017-08-22)
-------------------

- Change font-size #portal-top for mobile
  [mgennart]


0.5.14 (2017-08-22)
-------------------

- Change css for img.
  [mgennart]


0.5.13 (2017-08-16)
-------------------

- Add font mglabs in file fontello
  [mgennart]


0.5.12 (2017-08-03)
-------------------

- Fix data acquisition error on upgrade step.
  [bsuttor]


0.5.11 (2017-08-02)
-------------------

- Change css for slider.
   [mgennart]


0.5.10 (2017-07-26)
-------------------

- css adaptations.
  [mgennart]

0.5.9 (2017-07-24)
------------------

- Css adaptations.
  [bsuttor]


0.5.8 (2017-07-17)
------------------

- Update css.
  [osnickers]


0.5.7 (2017-07-17)
------------------

- Add upgrade to clean portal_skins from all cpskin (unused) skins / folders
  [laulaz]

- Fix icon-home commented code by mistake
  [laulaz]

- Change fields order on organization pages : #17751
  [laulaz]


0.5.6 (2017-07-06)
------------------

- Add fontello icon.
  [mgennart]


0.5.5 (2017-07-05)
------------------

- Change css for view facted list.
  [mgennart]

0.5.4 (2017-07-04)
------------------

- Change css for login page and view facted list
  [mgennart]


0.5.3 (2017-07-03)
------------------

- Add sticky right actions panel (for portlets and TOC) : #17748
  [laulaz]

- Fix: login_message fails if text field is empty.
  [bsuttor]


0.5.2 (2017-06-15)
------------------

- Many CSS changes
  [maud]

- Fix cookies messages on login form
  [laulaz]

- Fix LESS upgrade to keep CSS order even if reinstalled (which is the case
  during auto upgrade-portals) : #17714
  [laulaz]


0.5.1 (2017-05-31)
------------------

- Handle ploneCustom.css migration to LESS for both DTML method and File
  [laulaz]


0.5 (2017-05-29)
----------------

- Add dependency on cpskin.core (at install) to access banner_activation view
  [laulaz]

- Theme parameters harmonization
  [laulaz]

- Avoid explicit dependency to cpskin.minisite via a Diazo parameter. Use
  local method instead (with check on cpskin.minisite availability)
  [laulaz]

- Fix LESS files sort order in portal_less
  [laulaz]

- Setup initial LESS related code, files and migration from ploneCustom.css
  [laulaz]


0.4.14 (2017-05-10)
-------------------

- Duplicate CSS rules for now to handle #slider -> #slider-a-la-une and
  #carousel -> #carousel-a-la-une ids at the same time (#16991)
  [laulaz]


0.4.13 (2017-02-16)
-------------------

- Set version of profile.
  [bsuttor]


0.4.12 (2016-08-10)
-------------------

- If you add a document named 'login-message' on navigation root, its content will be visible on login form.
  [bsuttor]


0.4.11 (2016-06-13)
-------------------

- Add is_homepage and environment theme parameters
  [laulaz]

- Add is_homepage and environment views.
  [bsuttor]


0.4.10 (2016-04-19)
-------------------

- Remove rules that already exists in diazotheme.frameworks
  [laulaz]


0.4.9 (2016-01-12)
------------------

- Add css for collective.cookiecuttr integration.
  [bsuttor]


0.4.8 (2015-08-07)
------------------

- Remove .section-notheme #portal-breadcrumbs {display: none;}. Indeed, this code is now imported into homepage template directly.
  [bsuttor]

0.4.7 (2015-06-22)
------------------

- Nothing changed yet.


0.4.6 (2015-06-11)
------------------

- Nothing changed yet.


0.4.5 (2015-03-19)
------------------

- Fix randomly broken html (no head, ...)
  See details in http://trac.imio.be/trac/ticket/10615


0.4.4 (2015-02-19)
------------------

- Move Language selector to the top bar (#10069)
- Remove more elements from printed output


0.4.3 (2014-11-18)
------------------

- Change header position
- Minor improvements
- CSS cleanup


0.4.2 (2014-11-12)
------------------

- CSS changes


0.4.1 (2014-11-12)
------------------

- Fix natural orders (affinitic #6062)
- Change Diazo rules for more adaptability (affinitic #6062)


0.4 (2014-10-22)
----------------

- Add method to get current theme (affinitic #6038)
- Add CSS files taken out custom
- Minor fixes


0.3 (2014-10-07)
----------------

- Remove MenuTools viewlet (affinitic #6023)
- Use default Plone favicon mechanism (affinitic #5959)
- Use natural order for portal actions (affinitic #5972)
- Move social bookmarks icons to top (affinitic #5979)
- Remove Subject tags from Collection criteria and sort (affinitic #5899)
- Cleanup Diazo rules


0.2 (2014-08-21)
----------------

- Handle specific minisite layout for header, banner, breadcrumbs and footer
  (affinitic #5865)
- Show menutools viewlets on mobile (affinitic #5846)


0.1 (2014-07-02)
----------------

- Initial release
