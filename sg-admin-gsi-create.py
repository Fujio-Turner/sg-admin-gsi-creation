#!/usr/bin/python
import sys

indexNonXattr = []

bucket_name = 'cake'

if len(sys.argv) > 1 and isinstance(sys.argv[1],str):
	bucket_name = sys.argv[1]
else:
	print("You did give me a CB bucket name so I gave you 'cake'.")

index_replica = 0

if index_replica == 1:
	replica_str = ', "num_replica":1'
elif index_replica == 2:
	replica_str = ', "num_replica":2'
else:
	replica_str = ''

indexNonXattr.append('CREATE INDEX `sg_access_1` ON `'+bucket_name+'`((all (array (`op`.`name`) for `op` in object_pairs(((self.`_sync`).`access`)) end))) WITH { "defer_build":true '+replica_str+'};')

indexNonXattr.append('CREATE INDEX `sg_allDocs_1` ON `'+bucket_name+'`(((self.`_sync`).`sequence`),((self.`_sync`).`rev`),((self.`_sync`).`flags`),((self.`_sync`).`deleted`)) WHERE (not ((meta().`id`) like "\\_sync:%")) WITH { "defer_build":true '+replica_str+'};')

indexNonXattr.append('CREATE INDEX `sg_channels_1` ON `'+bucket_name+'`((all (array [(`op`.`name`), least(((self.`_sync`).`sequence`), ((`op`.`val`).`seq`)), ifmissing(((`op`.`val`).`rev`), null), ifmissing(((`op`.`val`).`del`), null)] for `op` in object_pairs(((self.`_sync`).`channels`)) end)),((self.`_sync`).`rev`),((self.`_sync`).`sequence`),((self.`_sync`).`flags`)) WITH { "defer_build":true '+replica_str+'};')

indexNonXattr.append('CREATE INDEX `sg_roleAccess_1` ON `'+bucket_name+'`((all (array (`op`.`name`) for `op` in object_pairs(((self.`_sync`).`role_access`)) end))) WITH { "defer_build":true '+replica_str+'};')

indexNonXattr.append('CREATE INDEX `sg_syncDocs_1` ON `'+bucket_name+'`((meta().`id`)) WHERE ((meta().`id`) like "\\_sync:%") WITH { "defer_build":true '+replica_str+'};')


buildIndex = 'BUILD INDEX ON `'+bucket_name+'`(`sg_access_1`,`sg_allDocs_1`,`sg_channels_1`,`sg_roleAccess_1`,`sg_syncDocs_1`) USING GSI;'


for x in indexNonXattr:
	print(x)
	print("")

print(buildIndex)
