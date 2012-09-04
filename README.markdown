# Brain Dump
A Django app for "dumping" ideas, thoughts, and breadcrumbs from the brain

# Installation
1. Navigate to your Django site folder (containing manage.py) and clone this repo using the command: `git clone https://github.com/bitflipr/brain_dump.git`
2. Add `brain\_dump` to the INSTALLED_APPS section in the settings.py file
3. Add the hard-coded path of the `brain_dump/templates` folder to the TEMPLATE\_DIRS section in the settings.py file 
4. Add `url(r'^dumps/', include('brain_dump.urls')),` to the urlpatterns in your site urls.py


# License
Brain Dump is licensed under the GNU General Public License Version 3 (GPL3). See the LICENSE file for more information.
