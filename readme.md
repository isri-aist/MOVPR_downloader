# Mapillary Omnidirectional Image Sequences Downloader

This short python script allows to download multiple images sequences from the *Mapillary* platform (read more at [https://www.mapillary.com/](https://www.mapillary.com/))

Given a file containing the `sequence_id` and the `image_id`s aimed for visual place recognition, the script downloads all required images to perform the evaluation of [Spherical VPR](https://github.com/isri-aist/sphericalVPR) implementations.

The file's header of each considered sequence is as follows:

`sequence_id`, `image_id`, `latitude`, `longitude`

And the pairs of sequences used for the vpr evaluation have the following header:

`sequence_id_database`, `sequence_id_query`, `image_id_database`, `image_id_query`, `latitude_database`, `longitude_database`, `latitude_query`, `longitude_query`

Please follow the instructions provided on the *Mapillary* website to obtain an access token to download the images, [here](https://www.mapillary.com/dashboard/developers)

Proposed sequences to download all follow the same constraints:

- **Omnidirectional images**
- Twice the same path travelled
- Different time of acquisition
- Same camera viewpoint

| City       | Type                   | Changing Conditions       | Covered Distance | Number of Images |
|------------|------------------------|---------------------------|------------------|------------------|
| Tsukuba (Japan) | Peri-urban road       | Luminosity change         | 14.4 km          | 536              |
| Paris (France)  | City streets          | Luminosity change         | 0.74 km          | 65               |
| Paris (France)  | City suburbs          | Season change             | 12.2 km          | 720              |
| Brussels (Belgium) | City streets       | Weather change            | 2.25 km          | 241              |
| Berlin (Germany) | City streets         | Weather change            | 1.75 km          | 158              |
| Countryside (France) | Country-side trail | Weather change            | 5.03 km          | 499              |
| Countryside (Japan) | Country-side road  | Spring / Winter           | 12.8 km          | 279              |
| **Total**  | -                      | -                         | **36.97 km**     | **1499**         |

Considered sequences of omnidirectional images are presented in this short video: [https://youtu.be/TEAkJhmcrLM](https://youtu.be/TEAkJhmcrLM)

## Dependencies

This python scripts relies on few and easy to install libraries:

- `os`
- `io`
- `pandas`
- `requests`
- `PIL`

## Credits

```
This software was developed at:
CNRS - AIST JRL (Joint Robotics Laboratory)
1-1-1 Umezono, Tsukuba, Ibaraki
Japan

This file is provided AS IS with NO WARRANTY OF ANY KIND, INCLUDING THE
WARRANTY OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.

Description:
Mapillary omnidirectional image sequences downloader
Authors:
Antoine ANDRE, Guillaume CARON

```
