from app.db import projects_collection

# Clear existing projects
projects_collection.delete_many({})

projects_collection.insert_many([

    # ---------------------------------------------------------
    # VREyeSAM
    # ---------------------------------------------------------
    {
        "slug": "vreyesam",
        "title": "VREyeSAM",
        "subtitle": "Virtual Reality Non-Frontal Iris Segmentation",

        # 🔗 External links (NEW)
        "links": {
            "GitHub Repository": "https://github.com/GeetanjaliGTZ/VREyeSAM.git",
            "Research Paper (ResearchGate)": "https://www.researchgate.net/publication/400248367_VREyeSAM_Virtual_Reality_Non-Frontal_Iris_Segmentation_using_Foundational_Model_with_uncertainty_weighted_loss"
        },

        "overview": [
            "VREyeSAM is a robust deep learning framework designed to address the unique challenges of iris segmentation in Virtual Reality (VR) environments.",
            "Unlike traditional biometric systems that rely on frontal, high-quality images, VR headsets such as the Meta Quest Pro capture ocular images affected by extreme non-frontal gaze angles, motion blur, partial occlusions from eyelids or eyelashes, and inconsistent illumination caused by near-infrared sensors."
        ],

        "technical_details": {
            "Technical Architecture & Innovations": [
                "VREyeSAM adapts Segment Anything Model 2 (SAM 2) as its foundational architecture, fine-tuned specifically for the iris domain.",
                "An uncertainty-weighted hybrid loss combines Focal Loss, Dice Loss, Binary Cross-Entropy (BCE), and entropy-based uncertainty weighting to focus learning on ambiguous regions such as boundaries and occlusions.",
                "Prompt-based supervision uses foreground point prompts sampled from ground-truth masks, guiding the Vision Transformer (ViT) encoder toward the iris region.",
                "A quality-aware preprocessing module automatically filters closed or partially closed eyes to ensure high-quality training and inference samples."
            ],
            "Training Setup": [
                "Evaluated on the VRBiom dataset using a curated subset named VRBiom-SegM.",
                "VRBiom-SegM contains approximately 100,000 manually annotated eye frames.",
                "Designed for robustness under non-frontal views and motion-induced artifacts."
            ]
        },

        "results": {
            "metrics": {
                "Precision": "0.751",
                "Recall": "0.870",
                "F1-Score": "0.806",
                "Mean IoU": "0.647"
            },
            "highlights": [
                "Significantly outperformed YOLOv11, PixlSegNet, and vanilla SAM 2.",
                "Maintained superior pixel-wise accuracy even under strict IoU thresholds.",
                "Validated suitability for real-time biometric systems in VR environments."
            ]
        }
    },

    # ---------------------------------------------------------
    # SEG-U-Sclera (SSBC 2025)
    # ---------------------------------------------------------
    {
        "slug": "ssbc",
        "title": "SEG-U-Sclera",
        "subtitle": "SSBC 2025 • IJCB",

        # 🔗 External link (NEW)
        "links": {
            "Research Paper (arXiv)": "https://arxiv.org/abs/2508.10737"
        },

        "overview": [
            "SEG-U-Sclera is the model submitted by Team IIT Mandi to the Sclera Segmentation Benchmarking Competition (SSBC 2025), held in conjunction with the International Joint Conference on Biometrics (IJCB 2025).",
            "The competition focused on developing privacy-preserving sclera segmentation models trained on synthetic data and benchmarking their generalization to real-world scenarios."
        ],

        "technical_details": {
            "Methodology & Approach": [
                "The approach fine-tuned the mask decoder of the SAM 2 architecture, comprising approximately 15 million trainable parameters.",
                "An uncertainty-weighted Binary Cross-Entropy (BCE) loss combined with a Score Loss was used to focus learning on ambiguous sclera boundaries and occlusions.",
                "Training leveraged both synthetic SynCROI data and real-world SBVPI samples for the Mixed Track.",
                "Data augmentations included horizontal flips, random rotations (±15°), and brightness scaling (0.7–1.3) to address capture-device variability."
            ]
        },

        "results": {
            "metrics": {
                "Rank (Mixed Track)": "6th (Global)",
                "Rank (Synthetic Track)": "7th (Global)",
                "F1 Score (MOBIUS)": "0.823",
                "F1 Score (SynMOBIUS)": "0.846"
            },
            "highlights": [
                "Demonstrated strong generalization when mixing synthetic and real data.",
                "Showed that architectural decisions were more impactful than data volume alone.",
                "Contributed to the IJCB 2025 benchmarking publication."
            ]
        }
    }
])

print("✅ Detailed project pages seeded successfully with links")
