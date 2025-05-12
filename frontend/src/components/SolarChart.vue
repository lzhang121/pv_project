<template>
    <div>
        <h2 class="text-xl font-bold mb-4">近7日太阳辐射强度（W/m²）</h2>
        <div ref="chart" style="height: 400px;"></div>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import * as echarts from 'echarts'

const chart = ref(null)

onMounted(async () => {
    const res = await fetch('/api/solar')
    const data = await res.json()

    const dates = data.map(d => d.date)
    const values = data.map(d => d.value)

    const myChart = echarts.init(chart.value)
    myChart.setOption({
        title: { text: '太阳辐射强度（过去7天）' },
        xAxis: { type: 'category', data: dates },
        yAxis: { type: 'value', name: 'W/m²' },
        tooltip: { trigger: 'axis' },
        series: [{
            name: '辐射强度',
            type: 'line',
            data: values,
            smooth: true,
            areaStyle: {},
        }]
    })
})
</script>
