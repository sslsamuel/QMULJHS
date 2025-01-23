dpl_enabled_blocks = ["Block1", "Block2"]
non_dpl_enabled_blocks = ["Block3", "Block4"]
invalid_dpl_enabled_blocks=dict(blockId="Block5", xptValidationViolationCode=404,errorDetails=["This block does not exist."],)


# response = dict(
#     initForDplBulkCancelResponse=dict(
#         sessionId=request["sessionId"],
#         dplEnabledBlockIds=dpl_enabled_blocks,
#         nonDplEnabledBlockIds=non_dpl_enabled_blocks,
#         invalidDplEnabledBlockIds=invalid_dpl_enabled_blocks,
#     )
# )

# response = {
    
#         {"sessionId": "1"},
#         {"dplEnabledBlocks": dpl_enabled_blocks},
#         {"nonDplEnabledBlocks": non_dpl_enabled_blocks},
#         {"invalidDplEnabledBlocks": [invalid_dpl_enabled_blocks]},
    
# }


x =  dict(

            sessionId="1",
            dplEnabledBlockIds=dpl_enabled_blocks,
            nonDplEnabledBlockIds=non_dpl_enabled_blocks,
            invalidDplEnabledBlockIds=[invalid_dpl_enabled_blocks],

    )

print(x)