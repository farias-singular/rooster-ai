```csharp
namespace Project.Application.UseCases.Brands.UpdateBrand
{
    public class UpdateBrandCommand : ICommand<UpdateBrandDto>
    {
        public string Id { get; }
        public string OrganizationId { get; }
        public Guid CategoryId { get; }
        public string Name { get; }
        public string? Title { get; }

        public UpdateBrandCommand(string id, string organizationId, Guid categoryId, string name, string? title)
        {
            Id = id;
            OrganizationId = organizationId;
            CategoryId = categoryId;
            Name = name;
            Title = title;
        }
    }
}
```