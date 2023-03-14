const {defineConfig} = require('@vue/cli-service')

module.exports = defineConfig(
    {
        transpileDependencies: true,
        devServer: {
            host: '0.0.0.0',
            allowedHosts: "all",
            proxy: {
                '^/api': {
                    target: 'http://flussberg.shop:8000',
                    ws: true,
                    changeOrigin: true
                }
            },
            hot: true,
        }
    }
)