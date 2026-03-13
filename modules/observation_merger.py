def merge_observations(observations):

    merged = []

    seen = set()

    for obs in observations:

        key = (obs["area"], obs["observation"])

        if key not in seen:

            seen.add(key)

            merged.append(obs)

    return merged