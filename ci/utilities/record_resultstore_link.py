#!/usr/bin/env python3
# Copyright 2026 The JAX Authors.
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
# ==============================================================================
# Records a pre-generated ResultStore link using GitHub Actions Annotations.
# Generates and returns (prints) the invocation_id to stdout.
# Prints the workflow notice command to stderr.

import sys
import uuid

def main():
  if len(sys.argv) < 2:
    print("Usage: record_resultstore_link.py <description>", file=sys.stderr)
    sys.exit(1)

  description = sys.argv[1]
  invocation_id = str(uuid.uuid4())

  # Print the ID to stdout so the calling script can capture it
  print(invocation_id)

  # Print the GHA notice to stderr so it is parsed by GHA but not captured by bash.
  # We use stderr because bash's INVOCATION_ID=$(...) only captures stdout.
  title = f"Bazel Results ({description})"
  message = f"Currently only visible to Googlers: https://source.cloud.google.com/results/invocations/{invocation_id}"
  
  # GitHub Actions workflow command syntax:
  # ::notice title={title}::{message}
  print(f"::notice title={title}::{message}", file=sys.stderr)

if __name__ == "__main__":
  main()
