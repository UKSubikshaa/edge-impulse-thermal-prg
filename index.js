const { ProcessingBlock } = require('edge-impulse-processing-block');

module.exports = new ProcessingBlock({
    name: 'thermal-prg',
    description: 'Thermal image processing block',
    process: async (data, config) => {
        return {
            features: data
        };
    }
});
