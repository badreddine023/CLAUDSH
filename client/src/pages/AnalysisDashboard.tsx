import { Card } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";
import { BarChart, Bar, LineChart, Line, HeatmapChart, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from "recharts";
import { Network, TrendingUp, Zap, BookOpen } from "lucide-react";

export default function AnalysisDashboard() {
  // Sample data for visualizations
  const entropyData = [
    { surah: "Al-Fatiha", entropy: 2.3, order: 1 },
    { surah: "Al-Baqarah", entropy: 3.1, order: 2 },
    { surah: "Al-Imran", entropy: 2.8, order: 3 },
    { surah: "An-Nisa", entropy: 3.2, order: 4 },
    { surah: "Al-Maidah", entropy: 2.9, order: 5 },
    { surah: "Al-Anam", entropy: 3.0, order: 6 },
  ];

  const markovData = [
    { order: 1, probability: 0.45 },
    { order: 2, probability: 0.38 },
    { order: 3, probability: 0.32 },
    { order: 4, probability: 0.28 },
    { order: 5, probability: 0.24 },
  ];

  const glocityData = [
    { surah: "Al-Fatiha", local: 0.8, global: 0.6, glocity: 0.48 },
    { surah: "Al-Baqarah", local: 0.7, global: 0.8, glocity: 0.56 },
    { surah: "Al-Imran", local: 0.75, global: 0.7, glocity: 0.525 },
    { surah: "An-Nisa", local: 0.72, global: 0.75, glocity: 0.54 },
    { surah: "Al-Maidah", local: 0.78, global: 0.65, glocity: 0.507 },
  ];

  const semanticFields = [
    { field: "Tawhid", frequency: 156, entropy: 2.1 },
    { field: "Prophecy", frequency: 142, entropy: 1.9 },
    { field: "Law", frequency: 198, entropy: 2.3 },
    { field: "Ethics", frequency: 167, entropy: 2.0 },
    { field: "Nature", frequency: 134, entropy: 1.8 },
    { field: "Hereafter", frequency: 189, entropy: 2.2 },
  ];

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-50 to-slate-100 dark:from-slate-950 dark:to-slate-900">
      {/* Header */}
      <div className="bg-white dark:bg-slate-900 border-b border-slate-200 dark:border-slate-800">
        <div className="container mx-auto px-4 py-8">
          <h1 className="text-4xl font-bold text-slate-900 dark:text-white mb-2">
            Analysis Dashboard
          </h1>
          <p className="text-slate-600 dark:text-slate-400">
            Explore linguistic patterns, information-theoretic metrics, and semantic networks
          </p>
        </div>
      </div>

      <div className="container mx-auto px-4 py-8">
        {/* Key Metrics */}
        <div className="grid grid-cols-1 md:grid-cols-4 gap-4 mb-8">
          {[
            { label: "Total Surahs", value: "114", icon: BookOpen },
            { label: "Avg Entropy", value: "2.85", icon: TrendingUp },
            { label: "Markov Order", value: "5", icon: Network },
            { label: "Semantic Fields", value: "10", icon: Zap }
          ].map((metric, idx) => (
            <Card key={idx} className="p-6">
              <div className="flex items-center justify-between">
                <div>
                  <p className="text-slate-600 dark:text-slate-400 text-sm">{metric.label}</p>
                  <p className="text-3xl font-bold text-slate-900 dark:text-white mt-2">
                    {metric.value}
                  </p>
                </div>
                <metric.icon className="w-8 h-8 text-blue-600 opacity-50" />
              </div>
            </Card>
          ))}
        </div>

        {/* Analysis Tabs */}
        <Tabs defaultValue="entropy" className="w-full">
          <TabsList className="grid w-full grid-cols-4 mb-8">
            <TabsTrigger value="entropy">Entropy Analysis</TabsTrigger>
            <TabsTrigger value="markov">Markov Chains</TabsTrigger>
            <TabsTrigger value="glocity">Glocality Score</TabsTrigger>
            <TabsTrigger value="semantic">Semantic Fields</TabsTrigger>
          </TabsList>

          {/* Entropy Analysis Tab */}
          <TabsContent value="entropy" className="space-y-6">
            <Card className="p-6">
              <h3 className="text-xl font-bold mb-4 text-slate-900 dark:text-white">
                Shannon Entropy by Surah
              </h3>
              <ResponsiveContainer width="100%" height={300}>
                <BarChart data={entropyData}>
                  <CartesianGrid strokeDasharray="3 3" />
                  <XAxis dataKey="surah" angle={-45} textAnchor="end" height={80} />
                  <YAxis />
                  <Tooltip />
                  <Legend />
                  <Bar dataKey="entropy" fill="#3b82f6" name="Entropy" />
                </BarChart>
              </ResponsiveContainer>
            </Card>

            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
              <Card className="p-6">
                <h4 className="font-bold mb-4 text-slate-900 dark:text-white">
                  Entropy Interpretation
                </h4>
                <ul className="space-y-3 text-sm text-slate-600 dark:text-slate-400">
                  <li className="flex gap-2">
                    <span className="text-blue-600 font-bold">•</span>
                    <span>High entropy indicates diverse vocabulary and complex structures</span>
                  </li>
                  <li className="flex gap-2">
                    <span className="text-blue-600 font-bold">•</span>
                    <span>Low entropy suggests repetitive patterns and focused themes</span>
                  </li>
                  <li className="flex gap-2">
                    <span className="text-blue-600 font-bold">•</span>
                    <span>Entropy varies across surahs based on revelation context</span>
                  </li>
                </ul>
              </Card>

              <Card className="p-6">
                <h4 className="font-bold mb-4 text-slate-900 dark:text-white">
                  Statistical Summary
                </h4>
                <div className="space-y-2 text-sm">
                  <div className="flex justify-between">
                    <span className="text-slate-600 dark:text-slate-400">Mean Entropy:</span>
                    <span className="font-bold text-slate-900 dark:text-white">2.85</span>
                  </div>
                  <div className="flex justify-between">
                    <span className="text-slate-600 dark:text-slate-400">Std Deviation:</span>
                    <span className="font-bold text-slate-900 dark:text-white">0.34</span>
                  </div>
                  <div className="flex justify-between">
                    <span className="text-slate-600 dark:text-slate-400">Min Entropy:</span>
                    <span className="font-bold text-slate-900 dark:text-white">2.3</span>
                  </div>
                  <div className="flex justify-between">
                    <span className="text-slate-600 dark:text-slate-400">Max Entropy:</span>
                    <span className="font-bold text-slate-900 dark:text-white">3.2</span>
                  </div>
                </div>
              </Card>
            </div>
          </TabsContent>

          {/* Markov Chains Tab */}
          <TabsContent value="markov" className="space-y-6">
            <Card className="p-6">
              <h3 className="text-xl font-bold mb-4 text-slate-900 dark:text-white">
                Markov Transition Probabilities by Order
              </h3>
              <ResponsiveContainer width="100%" height={300}>
                <LineChart data={markovData}>
                  <CartesianGrid strokeDasharray="3 3" />
                  <XAxis dataKey="order" label={{ value: "Markov Order", position: "insideBottomRight", offset: -5 }} />
                  <YAxis label={{ value: "Probability", angle: -90, position: "insideLeft" }} />
                  <Tooltip />
                  <Legend />
                  <Line type="monotone" dataKey="probability" stroke="#3b82f6" name="Transition Probability" strokeWidth={2} />
                </LineChart>
              </ResponsiveContainer>
            </Card>

            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
              <Card className="p-6">
                <h4 className="font-bold mb-4 text-slate-900 dark:text-white">
                  Markov Analysis Details
                </h4>
                <ul className="space-y-3 text-sm text-slate-600 dark:text-slate-400">
                  <li className="flex gap-2">
                    <Badge className="flex-shrink-0">1st Order</Badge>
                    <span>Word-to-word transitions (45% average probability)</span>
                  </li>
                  <li className="flex gap-2">
                    <Badge className="flex-shrink-0">2nd Order</Badge>
                    <span>Two-word sequences (38% average probability)</span>
                  </li>
                  <li className="flex gap-2">
                    <Badge className="flex-shrink-0">3rd-5th Order</Badge>
                    <span>Complex phrase patterns (24-32% probability)</span>
                  </li>
                </ul>
              </Card>

              <Card className="p-6">
                <h4 className="font-bold mb-4 text-slate-900 dark:text-white">
                  Key Findings
                </h4>
                <ul className="space-y-2 text-sm text-slate-600 dark:text-slate-400">
                  <li className="flex gap-2">
                    <span className="text-green-600 font-bold">✓</span>
                    <span>Deterministic grammatical sequences identified</span>
                  </li>
                  <li className="flex gap-2">
                    <span className="text-green-600 font-bold">✓</span>
                    <span>Absorbing states in POS transitions detected</span>
                  </li>
                  <li className="flex gap-2">
                    <span className="text-green-600 font-bold">✓</span>
                    <span>Stationary distributions calculated</span>
                  </li>
                </ul>
              </Card>
            </div>
          </TabsContent>

          {/* Glocality Score Tab */}
          <TabsContent value="glocity" className="space-y-6">
            <Card className="p-6">
              <h3 className="text-xl font-bold mb-4 text-slate-900 dark:text-white">
                Glocality Score: Local Cohesion × Global Connectedness
              </h3>
              <ResponsiveContainer width="100%" height={300}>
                <BarChart data={glocityData}>
                  <CartesianGrid strokeDasharray="3 3" />
                  <XAxis dataKey="surah" angle={-45} textAnchor="end" height={80} />
                  <YAxis />
                  <Tooltip />
                  <Legend />
                  <Bar dataKey="local" fill="#3b82f6" name="Local Cohesion" />
                  <Bar dataKey="global" fill="#8b5cf6" name="Global Connectedness" />
                  <Bar dataKey="glocity" fill="#ec4899" name="Glocality Score" />
                </BarChart>
              </ResponsiveContainer>
            </Card>

            <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
              <Card className="p-6">
                <h4 className="font-bold mb-4 text-slate-900 dark:text-white">
                  Local Cohesion
                </h4>
                <p className="text-sm text-slate-600 dark:text-slate-400 mb-4">
                  Average Markov probability within surah
                </p>
                <div className="space-y-2">
                  {glocityData.slice(0, 3).map((item, idx) => (
                    <div key={idx} className="flex justify-between text-sm">
                      <span className="text-slate-600 dark:text-slate-400">{item.surah}</span>
                      <span className="font-bold text-slate-900 dark:text-white">{item.local}</span>
                    </div>
                  ))}
                </div>
              </Card>

              <Card className="p-6">
                <h4 className="font-bold mb-4 text-slate-900 dark:text-white">
                  Global Connectedness
                </h4>
                <p className="text-sm text-slate-600 dark:text-slate-400 mb-4">
                  Degree centrality in cross-surah network
                </p>
                <div className="space-y-2">
                  {glocityData.slice(0, 3).map((item, idx) => (
                    <div key={idx} className="flex justify-between text-sm">
                      <span className="text-slate-600 dark:text-slate-400">{item.surah}</span>
                      <span className="font-bold text-slate-900 dark:text-white">{item.global}</span>
                    </div>
                  ))}
                </div>
              </Card>

              <Card className="p-6">
                <h4 className="font-bold mb-4 text-slate-900 dark:text-white">
                  Glocality Ranking
                </h4>
                <p className="text-sm text-slate-600 dark:text-slate-400 mb-4">
                  Combined local-global score
                </p>
                <div className="space-y-2">
                  {glocityData.slice(0, 3).map((item, idx) => (
                    <div key={idx} className="flex justify-between text-sm">
                      <span className="text-slate-600 dark:text-slate-400">{item.surah}</span>
                      <span className="font-bold text-slate-900 dark:text-white">{item.glocity}</span>
                    </div>
                  ))}
                </div>
              </Card>
            </div>
          </TabsContent>

          {/* Semantic Fields Tab */}
          <TabsContent value="semantic" className="space-y-6">
            <Card className="p-6">
              <h3 className="text-xl font-bold mb-4 text-slate-900 dark:text-white">
                Semantic Field Distribution
              </h3>
              <ResponsiveContainer width="100%" height={300}>
                <BarChart data={semanticFields}>
                  <CartesianGrid strokeDasharray="3 3" />
                  <XAxis dataKey="field" angle={-45} textAnchor="end" height={80} />
                  <YAxis />
                  <Tooltip />
                  <Legend />
                  <Bar dataKey="frequency" fill="#3b82f6" name="Frequency" />
                </BarChart>
              </ResponsiveContainer>
            </Card>

            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
              <Card className="p-6">
                <h4 className="font-bold mb-4 text-slate-900 dark:text-white">
                  Thematic Clusters
                </h4>
                <div className="space-y-3">
                  {semanticFields.map((field, idx) => (
                    <div key={idx} className="flex items-center justify-between">
                      <div className="flex items-center gap-2">
                        <div className="w-3 h-3 rounded-full" style={{
                          backgroundColor: `hsl(${idx * 60}, 70%, 50%)`
                        }}></div>
                        <span className="text-sm font-medium text-slate-900 dark:text-white">
                          {field.field}
                        </span>
                      </div>
                      <Badge variant="outline">{field.frequency}</Badge>
                    </div>
                  ))}
                </div>
              </Card>

              <Card className="p-6">
                <h4 className="font-bold mb-4 text-slate-900 dark:text-white">
                  Semantic Analysis
                </h4>
                <ul className="space-y-3 text-sm text-slate-600 dark:text-slate-400">
                  <li className="flex gap-2">
                    <span className="text-blue-600 font-bold">•</span>
                    <span>10 primary thematic clusters identified</span>
                  </li>
                  <li className="flex gap-2">
                    <span className="text-blue-600 font-bold">•</span>
                    <span>Co-occurrence matrices built across themes</span>
                  </li>
                  <li className="flex gap-2">
                    <span className="text-blue-600 font-bold">•</span>
                    <span>Theme transition probabilities calculated</span>
                  </li>
                  <li className="flex gap-2">
                    <span className="text-blue-600 font-bold">•</span>
                    <span>Evolution tracked across revelation timeline</span>
                  </li>
                </ul>
              </Card>
            </div>
          </TabsContent>
        </Tabs>

        {/* Additional Information */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mt-8">
          <Card className="p-6">
            <h3 className="text-xl font-bold mb-4 text-slate-900 dark:text-white">
              Visualization Options
            </h3>
            <ul className="space-y-3 text-sm text-slate-600 dark:text-slate-400">
              <li className="flex gap-2">
                <Badge>3D Network</Badge>
                <span>Revelation sequence vs. canonical order with information density</span>
              </li>
              <li className="flex gap-2">
                <Badge>Heatmap</Badge>
                <span>Surahs × Semantic fields with normalized frequency</span>
              </li>
              <li className="flex gap-2">
                <Badge>Markov Diagram</Badge>
                <span>State transitions with absorbing/recurrent states highlighted</span>
              </li>
            </ul>
          </Card>

          <Card className="p-6">
            <h3 className="text-xl font-bold mb-4 text-slate-900 dark:text-white">
              Export & Download
            </h3>
            <div className="space-y-2">
              <button className="w-full px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white rounded-lg text-sm font-medium transition-colors">
                Export as JSON
              </button>
              <button className="w-full px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white rounded-lg text-sm font-medium transition-colors">
                Export as CSV
              </button>
              <button className="w-full px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white rounded-lg text-sm font-medium transition-colors">
                Generate PDF Report
              </button>
            </div>
          </Card>
        </div>
      </div>
    </div>
  );
}
