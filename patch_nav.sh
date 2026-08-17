#!/bin/bash
set -e

# 1. CASES -> PROOF (both link and current-page span)
sed -i 's|>CASES<|>PROOF<|g' *.html

# 2. Insert ABOUT before the CONTACT nav line
sed -i '/<nav>/,/<\/nav>/ s|^\(<a href="contact.html">CONTACT</a>\)$|<a href="about.html">ABOUT</a>\n\1|' *.html
sed -i '/<nav>/,/<\/nav>/ s|^\(<span aria-current="page">CONTACT</span>\)$|<a href="about.html">ABOUT</a>\n\1|' *.html
