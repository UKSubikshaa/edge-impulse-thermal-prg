module.exports = async function (data, opts) {

    let features = [];

    for (let i = 0; i < data.length; i++) {

        let normalized = data[i] / 255;

        features.push(normalized);
    }

    return {
        features: features
    };
};
