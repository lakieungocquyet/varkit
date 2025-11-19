from modules.header import *

def default_pipeline(workflow_config, gvcf_file_string, known_sites_string):
    # [STAGE 1]: MAPPING AND ALIGNMENT
    mapping_and_alignment_flow(
        workflow_config = workflow_config
        )
    # [STAGE 2]: POST MAPPING AND ALIGNMENT
    post_mapping_and_alignment_flow(
        workflow_config = workflow_config, 
        known_sites_string = known_sites_string
        )
    # [STAGE 3]: VARIANT CALLING
    variant_calling_flow(
        workflow_config = workflow_config
        )
    # [STAGE 4]: POST VARIANT CALLING
    post_variant_calling_flow(
        workflow_config = workflow_config, 
        gvcf_file_string = gvcf_file_string
        )
    # [STAGE 5]: VARIANT ANNOTATION
    variant_annotation_flow(
        workflow_config = workflow_config
        )
    # [STAGE 6]: DOWNSTREAM PROCESSING
    downstream_processing_flow(
        workflow_config = workflow_config
    )
    return 0