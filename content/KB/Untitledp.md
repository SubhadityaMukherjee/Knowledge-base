```python
def proxy_one_batch(config, input_wrong, cam):
    grads = cam(input_tensor=input_wrong.to(config["device"]), targets=None)
    grads = torch.Tensor(grads).to(config["device"]).unsqueeze(1).expand(-1, 3, -1, -1)
    normalized_inps = inv_normalize(input_wrong)
    
    if config["pixel_replacement_method"] != "blended":
        output =  torch.where(
            grads > config["proxy_threshold"],
            dict_decide_change[config["pixel_replacement_method"](grads),
            normalized_inps,
        )
    else:
        output= torch.where(
            grads > config["proxy_threshold"],
            (1 - config["proxy_image_weight"] * grads) * normalized_inps,
            normalized_inps,
        )
    del grads
    return output

```
```python
def proxy_callback(config, input_wrong_full, label_wrong_full, cam):
    # TODO Save Classwise fraction
    chosen_inds = int(np.ceil(config["change_subset_attention"] * len(label_wrong_full)))
    # TODO some sort of decay?
    # TODO Remove min and batchify

    input_wrong_full = input_wrong_full[:chosen_inds]
    label_wrong_full = label_wrong_full[:chosen_inds]

    processed_labels = []
    processed_thresholds = []

    for i in tqdm(range(0, len(input_wrong_full), config["batch_size"]), desc="Running proxy"):
        try:
            input_wrong = input_wrong_full[i:i+config["batch_size"]
            label_wrong = label_wrong_full[i:i+config["batch_size"]

            try:
                input_wrong = torch.squeeze(torch.stack(input_wrong, dim=1))
                label_wrong = torch.squeeze(torch.stack(label_wrong, dim=1))
            except:
                input_wrong = torch.squeeze(input_wrong)
                label_wrong = torch.squeeze(label_wrong)

            thresholded_ims = proxy_one_batch(config, input_wrong.to(config["device"]), cam)
            processed_thresholds.extend(thresholded_ims.detach().cpu())
            processed_labels.extend(label_wrong)


    processed_thresholds = torch.stack(processed_thresholds, dim = 0).detach()
    batch_size = processed_thresholds.size(0)

    for ind in tqdm(range(batch_size), total=batch_size, desc="Saving images"):
        label = config["label_map"][processed_labels[ind].item()]
        save_name = (
            config["ds_path"] / label / f"proxy-{ind}-{config['global_run_count']}.jpeg"
        )
        tfm(processed_thresholds[ind, :, :, :]).save(save_name)

```



