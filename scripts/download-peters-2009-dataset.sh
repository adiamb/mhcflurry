#!/usr/bin/env bash

# Copyright (c) 2015. Mount Sinai School of Medicine
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Download 2009 subset dataset from Kim/Peters
# 2013 "Dataset size and composition" paper
rm -f bdata.2009.mhci.public.1*
wget https://dl.dropboxusercontent.com/u/3967524/bdata.2009.mhci.public.1.txt
DATA_DIR=`python -c "import mhcflurry; print(mhcflurry.paths.CLASS1_DATA_DIRECTORY)"`
mkdir -p -- "$DATA_DIR"
mv bdata.2009.mhci.public.1.txt "$DATA_DIR"
