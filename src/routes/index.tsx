import { createFileRoute } from "@tanstack/react-router";
import { CodigoAguiaLanding } from "@/components/landing/CodigoAguiaLanding";

const BASE_URL = "https://ocodigoaguia.com.br";

export const Route = createFileRoute("/")({
  component: CodigoAguiaLanding,
  head: () => ({
    meta: [
      { title: "O Código Águia — Mentalidade, Disciplina e Riqueza na Era Digital" },
      {
        name: "description",
        content:
          "Desenvolva a mentalidade, disciplina e visão estratégica para construir riqueza e liberdade na era digital. eBook premium para empreendedores.",
      },
      { property: "og:title", content: "O Código Águia — eBook Premium" },
      {
        property: "og:description",
        content: "Um sistema para construir liberdade e prosperidade na era digital.",
      },
      { property: "og:type", content: "website" },
      { property: "og:url", content: BASE_URL },
      { name: "twitter:card", content: "summary_large_image" },
      { name: "twitter:title", content: "O Código Águia — eBook Premium" },
      {
        name: "twitter:description",
        content: "Um sistema para construir liberdade e prosperidade na era digital.",
      },
      { tagName: "link", rel: "canonical", href: BASE_URL },
    ],
  }),
});
