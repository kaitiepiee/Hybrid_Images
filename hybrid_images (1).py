import typing as T
import numpy as np
import cv2
import imageio

# Do not import additional modules, otherwise, there will be deductions


def hybrid_images(image_high: T.Union[str, np.ndarray], image_low: T.Union[str, np.ndarray], output_file: str = None) -> np.ndarray:
    """
    Creates a hybrid image by combining a high-pass filtered version of the first input image
    with a low-pass filtered version of the second input image. The resulting image is `a`
    mixture of the high-frequency content of the first image and the low-frequency content of
    the second image.

    Args:
        image_high (Union[str, np.ndarray]): The first input image, either a filename (str) or a numpy array of shape CxHxW.
        image_low (Union[str, np.ndarray]): The second input image, either a filename (str) or a numpy array of shape CxHxW.
        output_file (str, optional): The filename to save the resulting image if not None.

    Returns:
        np.ndarray: The resulting hybrid image, as a numpy array (always returns a value)
    """

    img1= cv2.imread(image_low)
    img2= cv2.imread(image_high)

    img1= cv2.GaussianBlur(img1, (7,7), cv2.BORDER_DEFAULT)
    img2= cv2.GaussianBlur(img2, (13,13), cv2.BORDER_DEFAULT)

    hybrid = img1 - img2

    if output_file is not None:
        cv2.imwrite(output_file, hybrid)

    return hybrid

if __name__ == "__main__":
    image = hybrid_images('image_high.jpg', 'image_low.jpg', "image_hybrid.png")  # Find images on your own
    cv2.imshow('Hybrid Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# reference
# https://www.youtube.com/watch?v=26WcejEyQKc&t=109s&ab_channel=ousam2010
# https://jeremykun.com/2014/09/29/hybrid-images/