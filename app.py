import time 

from easyanimate.api.api import infer_forward_api, update_diffusion_transformer_api, update_edition_api
from easyanimate.ui.ui import ui_modelscope, ui, ui_huggingface

if __name__ == "__main__":
    # Choose the ui mode  
    ui_mode = "huggingface"
    # Server ip
    server_name = "0.0.0.0"
    server_port = 7860

    # Params below is used when ui_mode = "modelscope"
    edition = "v2"
    config_path = "config/easyanimate_video_magvit_motion_module_v2.yaml"
    model_name = "models/Diffusion_Transformer/EasyAnimateV2-XL-2-512x512"
    savedir_sample = "samples"

    if ui_mode == "modelscope":
        demo, controller = ui_modelscope(edition, config_path, model_name, savedir_sample)
    elif ui_mode == "huggingface":
        demo, controller = ui_huggingface(edition, config_path, model_name, savedir_sample)
    else:
        demo, controller = ui()

    # launch gradio
    app, _, _ = demo.queue(status_update_rate=1).launch(
        server_name=server_name,
        server_port=server_port,
        prevent_thread_lock=True
    )
    
    # launch api
    infer_forward_api(None, app, controller)
    update_diffusion_transformer_api(None, app, controller)
    update_edition_api(None, app, controller)
    
    # not close the python
    while True:
        time.sleep(5)