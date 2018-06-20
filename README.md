# sg-admin-gsi-creation
Simple Script for Couchbase Admins to create GSI indexes for Sync Gateway 2.1+

# WHY
Not all deployments give Sync Gateway full access to a bucket.
So an Administrator might need to make the indexes so sync gateway does not have a fit.


# HOW TO RUN

./sg-admin-gsi-create.py (name of your bucket Example 'cake')

# OUTPUT

CREATE INDEX `sg_access_1` ON `cake`((all (array (`op`. .....

CREATE INDEX `sg_allDocs_1` ON `cake`(((self.`_sync`).`s.....

CREATE INDEX `sg_roleAccess_1` ON `cake`((all (array (`o.....

CREATE INDEX `sg_syncDocs_1` ON `cake`((meta().`id`)) WH.....

BUILD INDEX ON `cake`(`sg_access_1`,`sg_allDocs_1`,`sg_c.....

# Requirements

Python 2.+
