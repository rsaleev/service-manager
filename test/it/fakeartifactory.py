#!/usr/bin/python

from bottle import route, run, request
from bottle import static_file

MAVEN_METADATA="""<?xml version="1.0" encoding="UTF-8"?>
<metadata>
  <groupId>uk.gov.hmrc</groupId>
  <artifactId>help-frontend_2.11</artifactId>
  <version>1.26.0</version>
  <versioning>
    <latest>1.26.0</latest>
    <release>1.26.0</release>
    <versions>
      <version>1.26.0-1-gd0dba7c</version>
      <version>1.26.0-2-gd213a4f</version>
      <version>1.26.0</version>
    </versions>
    <lastUpdated>20150804143826</lastUpdated>
  </versioning>
</metadata>"""

ASSETS_METADATA="""<?xml version="1.0" encoding="UTF-8"?>
<metadata modelVersion="1.1.0">
  <groupId>foo.bar.foo</groupId>
  <artifactId>assets-frontend</artifactId>
  <versioning>
    <latest>0.17.0</latest>
    <release>0.17.0</release>
    <versions>
      <version>0.14.0</version>
      <version>0.17.0</version>
    </versions>
    <lastUpdated>20180610040219</lastUpdated>
  </versioning>
</metadata>
"""


@route('/ping')
def ping():
    return "pong"

@route("/artifactory/hmrc-releases/foo/bar/foo/assets-frontend/maven-metadata.xml")
def search_xml():
  return ASSETS_METADATA

@route('/<filepath:path>')
def server_static(filepath):
  return static_file(filepath, root="./static/repositories")

@route('/artifactory/hmrc-releases/uk/gov/hmrc/playtest_2.11/maven-metadata.xml')
def maven_metadata():
    return MAVEN_METADATA

@route('/artifactory/hmrc-releases/uk/gov/hmrc/playtest_2.11/1.26.0/playtest_2.11-1.26.0.tgz')
def server_static_tgz():
    return static_file("bintray/playtest.tgz", root="./static/")

@route('/artifactory/hmrc-releases/uk/gov/hmrc/playtest_2.11/1.26.0/playtest_2.11-1.26.0.tgz.md5')
def server_static_md5():
    return static_file("bintray/playtest.tgz.md5", root="./static/")

run(host='localhost', port=8062)
