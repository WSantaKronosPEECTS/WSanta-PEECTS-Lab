# 🔄 PEECTS Live Dashboard

This dashboard auto-refreshes every 60 seconds.

## 🔧 Workflow Status

<div id="workflow-status" style="padding:10px; background:#f5f5f5; border-radius:8px;">
    Loading latest workflow status...
</div>

<script>
async function refreshWorkflow() {
    const url = "https://api.github.com/repos/WSantaKronos/WSantaPEECTS-Lab/actions/workflows/publish-release.yml/runs?per_page=1";

    try {
        const response = await fetch(url);
        const data = await response.json();
        const run = data.workflow_runs[0];

        const statusHTML = `
            <strong>Name:</strong> publish-release.yml<br>
            <strong>Status:</strong> ${run.status}<br>
            <strong>Conclusion:</strong> ${run.conclusion}<br>
            <strong>Last Update:</strong> ${new Date(run.updated_at).toLocaleString()}<br>
            <br>
            <a href="${run.html_url}" target="_blank">View on GitHub →</a>
        `;

        document.getElementById("workflow-status").innerHTML = statusHTML;

    } catch (error) {
        document.getElementById("workflow-status").innerHTML =
            "⚠️ Cannot load workflow status.";
    }
}

refreshWorkflow();                  // Load immediately
setInterval(refreshWorkflow, 60000); // Refresh every 60s
</script>
