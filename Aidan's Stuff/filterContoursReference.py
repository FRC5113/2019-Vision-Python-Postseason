@staticmethod
def __filter_contours(
    input_contours,
    min_area,
    min_perimeter,
    min_width,
    max_width,
    min_height,
    max_height,
    solidity,
    max_vertex_count,
    min_vertex_count,
    min_ratio,
    max_ratio,
):
    """Filters out contours that do not meet certain criteria.
    Args:
        input_contours: Contours as a list of numpy.ndarray.
        min_area: The minimum area of a contour that will be kept.
        min_perimeter: The minimum perimeter of a contour that will be kept.
        min_width: Minimum width of a contour.
        max_width: MaxWidth maximum width.
        min_height: Minimum height.
        max_height: Maximimum height.
        solidity: The minimum and maximum solidity of a contour.
        min_vertex_count: Minimum vertex Count of the contours.
        max_vertex_count: Maximum vertex Count.
        min_ratio: Minimum ratio of width to height.
        max_ratio: Maximum ratio of width to height.
    Returns:
        Contours as a list of numpy.ndarray.
    """
    # FOR THIS TO WORK YOU MUST
    # replace this
    # output = []

    # with this
    # output = [[], [], [], [], [], [], []]

    output = [[], [], [], [], [], [], []]
    for contour in input_contours:
        x, y, w, h = cv2.boundingRect(contour)
        if w < min_width or w > max_width:
            continue
        if h < min_height or h > max_height:
            continue
        area = cv2.contourArea(contour)
        if area < min_area:
            continue
        if cv2.arcLength(contour, True) < min_perimeter:
            continue
        hull = cv2.convexHull(contour)
        solid = 100 * area / cv2.contourArea(hull)
        if solid < solidity[0] or solid > solidity[1]:
            continue
        if len(contour) < min_vertex_count or len(contour) > max_vertex_count:
            continue
        ratio = (float)(w) / h
        if ratio < min_ratio or ratio > max_ratio:
            continue

        # FOR THIS TO WORK YOU MUST
        # replace this
        # output.append(contour)

        # with this
        # output[0].append(x)
        # output[1].append(y)
        # output[2].append(w)
        # output[3].append(h)
        # output[4].append(area)
        # output[5].append(solid)
        # output[6].append(ratio)

        output[0].append(x)
        output[1].append(y)
        output[2].append(w)
        output[3].append(h)
        output[4].append(area)
        output[5].append(solid)
        output[6].append(ratio)
    return output
